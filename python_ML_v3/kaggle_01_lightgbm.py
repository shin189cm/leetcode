"""
LightGBM K-Fold Pipeline (Regression Example)
- Dataset: California Housing
- Objective: Predict target value using LightGBM Regressor
- Validation: 5-Fold Cross Validation with Out-of-Fold (OOF) evaluation
- Metric: Root Mean Squared Error (RMSE)
"""

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import KFold


def main() -> None:
    # 1. データの読み込み
    dataset = fetch_california_housing(as_frame=True)
    df = dataset.frame
    target_col = dataset.target_names[0]

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 2. バリデーション設計 (5-Fold CV)
    n_splits = 5
    cv = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    # OOF予測値を格納する配列（行数と同じ長さのゼロ配列で初期化）
    oof_preds = np.zeros(len(X))
    models: list[lgb.LGBMRegressor] = []
    feature_importances = pd.DataFrame()

    # 3. K-Fold ループ
    for fold, (train_idx, val_idx) in enumerate(cv.split(X, y)):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]

        # ※前処理を行う場合はここで実装（必ず X_train で fit して X_val を transform）

        # 4. モデルの定義と学習（各Foldごとに新規インスタンス化）
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
                lgb.log_evaluation(period=0),
            ],
        )

        # 5. OOF予測の格納と各Foldのスコア検証
        val_pred = model.predict(X_val)
        oof_preds[val_idx] = val_pred
        fold_rmse = root_mean_squared_error(y_val, val_pred)
        print(f"Fold {fold + 1} RMSE: {fold_rmse:.4f}")

        # モデルと特徴量重要度を記録
        models.append(model)
        fold_importance = pd.DataFrame(
            {
                "feature": X.columns,
                "importance": model.feature_importances_,
                "fold": fold + 1,
            }
        )
        feature_importances = pd.concat(
            [feature_importances, fold_importance], axis=0
        )

    # 6. 全体（Out-of-Fold）スコアの評価
    overall_rmse = root_mean_squared_error(y, oof_preds)
    print(f"\n==============================")
    print(f"Overall OOF RMSE: {overall_rmse:.4f}")
    print(f"==============================")

    # 7. 全Fold平均の特徴量重要度を確認
    mean_importance = (
        feature_importances.groupby("feature")["importance"]
        .mean()
        .reset_index()
        .sort_values("importance", ascending=False)
    )
    print("\nTop 5 Important Features (Mean across 5 folds):")
    print(mean_importance.head(5))

    # 8. （参考）新規データ/テストデータに対する推論（アンサンブル平均）
    # test_preds = np.mean([m.predict(X_test) for m in models], axis=0)


if __name__ == "__main__":
    main()