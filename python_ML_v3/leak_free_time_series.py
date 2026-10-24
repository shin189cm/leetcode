import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

"""_summary_
【Step 1: データ前準備 (Pandas)】
1. データを timestamp 昇順でソート (df.sort_values + reset_index)
2. 説明変数 X, 目的変数 y, 日時列 を切り出す

【Step 2: パイプラインの設計 (scikit-learn)】
3. 列ごとの前処理レシピを定義 (ColumnTransformer)
    - 欠損値補完 (SimpleImputer)
    - スケーリング (StandardScaler)
    - カテゴリ変数変換 (OneHotEncoder)
4. モデル（Ridge等）と結合して 1 つの Pipeline にする

【Step 3: 時系列CVの分割・検証 (TimeSeriesSplit)】
5. TimeSeriesSplit オブジェクトを生成 (n_splits を指定)
6. for (train_idx, val_idx) in tscv.split(X):
    a. 【防御】Trainの最大時刻 <= Valの最小時刻 を assert で検証
    b. pipeline.fit(X_train, y_train)  <- Train のみで統計量を学習
    c. y_pred = pipeline.predict(X_val) <- Val は学習済みの統計量で変換・推論
    d. RMSE と R2_score を計算・記録
"""
# 前段で作成したダミーデータ生成関数を使用
from data_generator import generate_synthetic_data


def run_leak_free_time_series_cv(df: pd.DataFrame, n_splits: int = 4) -> None:
    # 1. 必須前提: 時系列昇順で厳密にソートし、インデックスを再採番
    df = df.sort_values("timestamp").reset_index(drop=True)

    features = ["category", "page_views", "discount_rate"]
    X = df[features]
    y = df["amount"]
    timestamps = df["timestamp"]

    # 2. 前処理パイプラインの定義 (GroupKFold時と同一)
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline([
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]),
                ["page_views", "discount_rate"],
            ),
            (
                "cat",
                Pipeline([
                    ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                ]),
                ["category"],
            ),
        ],
        remainder="drop",
    )

    full_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", Ridge(alpha=1.0)),
    ])

    # 3. TimeSeriesSplit による交差検証 (ローリング/拡張ウィンドウ)
    tscv = TimeSeriesSplit(n_splits=n_splits)

    rmse_scores = []
    r2_scores = []

    print(f"=== TimeSeriesSplit Cross Validation (n_splits={n_splits}) ===")

    for fold, (train_idx, val_idx) in enumerate(tscv.split(X), start=1):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]

        time_train_max = timestamps.iloc[train_idx].max()
        time_val_min = timestamps.iloc[val_idx].min()

        # 【検証】未来データのリークがないかアサーション (Trainの最大時刻 <= Validの最小時刻)
        assert time_train_max <= time_val_min, (
            f"Fold {fold}: Lookahead leakage detected! "
            f"Train max ({time_train_max}) > Val min ({time_val_min})"
        )

        # 学習 & 予測 (過去のデータのみでfit)
        full_pipeline.fit(X_train, y_train)
        y_pred = full_pipeline.predict(X_val)

        rmse = np.sqrt(mean_squared_error(y_val, y_pred))
        r2 = r2_score(y_val, y_pred)

        rmse_scores.append(rmse)
        r2_scores.append(r2)

        print(
            f"Fold {fold} | "
            f"Train: {len(train_idx)} records ({timestamps.iloc[train_idx].min():%m/%d} ~ {time_train_max:%m/%d}) | "
            f"Val: {len(val_idx)} records ({time_val_min:%m/%d} ~ {timestamps.iloc[val_idx].max():%m/%d}) | "
            f"Val RMSE: {rmse:.2f} | Val R2: {r2:.4f}"
        )

    print("--------------------------------------------------")
    print(f"Mean RMSE: {np.mean(rmse_scores):.2f} (±{np.std(rmse_scores):.2f})")
    print(f"Mean R2  : {np.mean(r2_scores):.4f} (±{np.std(r2_scores):.4f})")


if __name__ == "__main__":
    df = generate_synthetic_data(n_records=1000, n_customers=100, seed=42)
    run_leak_free_time_series_cv(df)