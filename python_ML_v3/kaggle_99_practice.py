# 値の予測
# cross validaton
# LightGBM

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import KFold

def main() -> None:
    # california特有の処理
    dataset = fetch_california_housing(as_frame=True)
    df = dataset.frame
    target_col = dataset.target_names[0]

    X = df.drop(columns=[target_col]) # 目的変数を外す。完全なるリークになっちゃう。
    y = df[target_col]

    # cross validationの設計をする
    n_splits = 5
    cv = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    # out of foldの予測値を格納する配列
    oof_preds = np.zeros(len(X))
    models: list[lgb.LGBMRegressor] = [] # 回帰の結果のモデルを格納するリスト
    feature_importances = pd.DataFrame()

    # K-Foldのループ
    for fold, (train_idx, val_idx) in enumerate(cv.split(X, y)):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val  = X.iloc[val_idx], y.iloc[val_idx]

        model = lgb.LGBMRegressor(
            n_estimators = 1000,
            learning_rate = 0.05,
            random_state= 42,
            n_jobs = -1,
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

        val_pred = model.predict(X_val)
        oof_preds[val_idx] = val_pred
        fold_rmse = root_mean_squared_error(y_val, val_pred)
        print(f"Fold {fold + 1} RMSE: {fold_rmse:.4f}")

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

    overall_rmse = root_mean_squared_error(y, oof_preds)
    print(f"\n==============================")
    print(f"Overall OOF RMSE: {overall_rmse:.4f}")
    print(f"==============================")

    mean_importance = (
        feature_importances.groupby("feature")["importance"]
        .mean()
        .reset_index()
        .sort_values("importance", ascending=False)
    )
    print("\nTop 5 Important Features (Mean across 5 folds)")
    print(mean_importance.head(5))

if __name__ == "__main__":
    main()