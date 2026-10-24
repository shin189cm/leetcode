import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

import numpy as np
import pandas as pd


def generate_synthetic_data(n_records: int = 1000, n_customers: int = 100, seed: int = 42) -> pd.DataFrame:
    """リークのない前処理・CV設計検証用のダミーEC取引データを生成する。

    Parameters
    ----------
    n_records : int
        総レコード数
    n_customers : int
        ユニーク顧客数
    seed : int
        乱数シード

    Returns
    -------
    pd.DataFrame
        ダミー取引データ
    """
    rng = np.random.default_rng(seed)

    # 1. 顧客ID (偏りを持たせてリピート客を表現)
    customer_pool = [f"CUST_{i:04d}" for i in range(n_customers)]
    customer_probs = rng.dirichlet(np.ones(n_customers) * 0.5)
    customer_ids = rng.choice(customer_pool, size=n_records, p=customer_probs)

    # 2. 取引日時 (2026年1月〜4月の時系列データ)
    start_date = np.datetime64("2026-01-01T00:00:00")
    # 秒単位のランダムオフセット
    seconds_offset = rng.integers(0, 100 * 24 * 3600, size=n_records)
    timestamps = start_date + seconds_offset.astype("timedelta64[s]")

    # 3. 特徴量
    # カテゴリ（カテゴリカル変数・Target Encoding検証用）
    categories = ["electronics", "apparel", "books", "food", "beauty"]
    product_category = rng.choice(categories, size=n_records, p=[0.2, 0.3, 0.2, 0.2, 0.1])

    # 閲覧ページ数（欠損を含む数値特徴量）
    views = rng.poisson(lam=5, size=n_records).astype(float)
    # 5%の確率で欠損値を注入
    mask_nan = rng.random(size=n_records) < 0.05
    views[mask_nan] = np.nan

    # 割引率 (0.0 〜 0.3)
    discount_rate = rng.choice([0.0, 0.05, 0.1, 0.2, 0.3], size=n_records)

    # 4. 目的変数: 購入金額 (amount)
    # シグナル + ノイズで生成（時間経過による緩やかなベースアップも加味）
    base_price = {"electronics": 25000, "apparel": 6000, "books": 1800, "food": 3500, "beauty": 4500}
    cat_price = np.array([base_price[c] for c in product_category])

    # 欠損補正前のビュー数ベース
    clean_views = np.nan_to_num(views, nan=5.0)
    # 時間経過トレンド (後半ほど高額化)
    time_trend = (seconds_offset / (100 * 24 * 3600)) * 2000

    amount = (
        cat_price * (1 - discount_rate)
        + clean_views * 500
        + time_trend
        + rng.normal(0, 1000, size=n_records)
    )
    # マイナス防止と四捨五入
    amount = np.maximum(amount, 500).round()

    df = pd.DataFrame({
        "timestamp": timestamps,
        "customer_id": customer_ids,
        "category": product_category,
        "page_views": views,
        "discount_rate": discount_rate,
        "amount": amount,
    })

    # 時系列順にソートしておく
    df = df.sort_values("timestamp").reset_index(drop=True)
    return df

if __name__ == "__main__":
    df = generate_synthetic_data()
    print("データ形状:", df.shape)
    print("\n欠損値の数:\n", df.isnull().sum())
    print("\nユニーク顧客数:", df["customer_id"].nunique())
    print("\n先頭5行:\n", df.head())

# from data_generator import generate_synthetic_data


def run_leak_free_group_kfold_cv(df: pd.DataFrame, n_splits: int = 5) -> None:
    # 1. 説明変数・目的変数・グループの分離
    features = ["category", "page_views", "discount_rate"]
    X = df[features]
    y = df["amount"]
    groups = df["customer_id"]

    # 2. 前処理パイプラインの定義 (ColumnTransformer)
    num_features = ["page_views", "discount_rate"]
    cat_features = ["category"]

    # 数値特徴量: 欠損値補完 (中央値) -> 標準化
    # ※ fit_transform時にTrainセットの中央値と平均・分散のみが算出・保持される
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    # カテゴリ特徴量: One-Hot Encoding
    # ※ handle_unknown='ignore' でValidに未知のカテゴリが出現してもエラーにならず0埋め
    cat_pipeline = Pipeline([
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_pipeline, num_features),
            ("cat", cat_pipeline, cat_features),
        ],
        remainder="drop",
    )

    # 3. モデルを結合したフルパイプライン
    full_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", Ridge(alpha=1.0)),
    ])

    # 4. GroupKFold による交差検証
    gkf = GroupKFold(n_splits=n_splits)

    rmse_scores = []
    r2_scores = []

    print(f"=== GroupKFold Cross Validation (n_splits={n_splits}) ===")

    for fold, (train_idx, val_idx) in enumerate(gkf.split(X, y, groups=groups), start=1):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
        groups_train = set(groups.iloc[train_idx])
        groups_val = set(groups.iloc[val_idx])

        # 【検証】顧客IDの交差（リーク）がないかアサーション
        overlap = groups_train.intersection(groups_val)
        assert len(overlap) == 0, f"Fold {fold}: Group overlap detected: {overlap}"

        # 学習 & 予測
        # fit: X_train の統計量のみを学習
        full_pipeline.fit(X_train, y_train)

        # predict: X_train で得た統計量を使って X_val を transform し推論
        y_pred = full_pipeline.predict(X_val)

        # 評価指標計算
        rmse = np.sqrt(mean_squared_error(y_val, y_pred))
        r2 = r2_score(y_val, y_pred)

        rmse_scores.append(rmse)
        r2_scores.append(r2)

        print(
            f"Fold {fold} | "
            f"Train Size: {len(X_train)} (Groups: {len(groups_train)}) | "
            f"Val Size: {len(X_val)} (Groups: {len(groups_val)}) | "
            f"Val RMSE: {rmse:.2f} | "
            f"Val R2: {r2:.4f}"
        )

    print("--------------------------------------------------")
    print(f"Mean RMSE: {np.mean(rmse_scores):.2f} (±{np.std(rmse_scores):.2f})")
    print(f"Mean R2  : {np.mean(r2_scores):.4f} (±{np.std(r2_scores):.4f})")


if __name__ == "__main__":
    # 動作確認用データ生成
    from io import StringIO

    # ダミーデータ生成コードを実行して df を取得
    # from data_generator import generate_synthetic_data  # 外部ファイルまたは同スクリプト

    df = generate_synthetic_data(n_records=1000, n_customers=100, seed=42)
    run_leak_free_group_kfold_cv(df)