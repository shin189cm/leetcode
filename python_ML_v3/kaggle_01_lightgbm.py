"""
LightGBM Baseline Pipeline (Regression Example)
- Dataset: California Housing
- Objective: Predict target value using LightGBM Regressor
- Validation: Train/Validation Split (Hold-out)
- Metric: Root Mean Squared Error (RMSE)
"""

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split


def main() -> None:
    # 1. データの読み込み
    # 実際の選考では pd.read_csv("train.csv") や BigQuery からの抽出を想定
    dataset = fetch_california_housing(as_frame=True)
    df = dataset.frame
    target_col = dataset.target_names[0]

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 2. バリデーション設計 (Train / Validation 分割)
    # ※ 時系列データなら TimeSeriesSplit / Temporal Split、
    # ※ 不均衡分類なら stratify=y、グループ重複があるなら GroupKFold を選択する
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. モデルの定義と学習
    # 早期打ち切り (early stopping) は過学習防止と学習時間の短縮に必須
    model = lgb.LGBMRegressor(
        n_estimators=1000,
        learning_rate=0.05,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(
        X_train,
        y_train,
        eval_set=[(X_val, y_val)],
        callbacks=[
            lgb.early_stopping(stopping_rounds=50, verbose=False),
            lgb.log_evaluation(period=0),  # ログを抑制したい場合は0
        ],
    )

    # 4. 検証と評価
    val_preds = model.predict(X_val)
    rmse = root_mean_squared_error(y_val, val_preds)
    print(f"Validation RMSE: {rmse:.4f}")

    # 5. 特徴量重要度の確認（ベースライン分析の初手）
    feature_importance = pd.DataFrame(
        {"feature": X.columns, "importance": model.feature_importances_}
    ).sort_values("importance", ascending=False)
    print("\nTop 5 Important Features:")
    print(feature_importance.head(5))


if __name__ == "__main__":
    main()