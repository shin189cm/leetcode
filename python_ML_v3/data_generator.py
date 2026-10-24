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
