"""
LightGBM K-Fold Pipeline (Binary Classification Example)
- Dataset: Breast Cancer Wisconsin
- Objective: Predict binary target (0 or 1) using LightGBM Classifier
- Validation: 5-Fold Stratified Cross Validation with OOF evaluation
- Metric: ROC-AUC
"""

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold  # 1. StratifiedKFold に変更

import matplotlib.pyplot as plt
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    PrecisionRecallDisplay,
    RocCurveDisplay,
)


def main() -> None:
    # 1. データの読み込み
    dataset = load_breast_cancer(as_frame=True)
    df = dataset.frame
    target_col = "target"

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 2. バリデーション設計（層化抽出）
    n_splits = 5
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    oof_preds = np.zeros(len(X))
    models: list[lgb.LGBMClassifier] = []

    # 3. K-Fold ループ (StratifiedKFold には split(X, y) と y を渡す)
    for fold, (train_idx, val_idx) in enumerate(cv.split(X, y)):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]

        # 4. モデル定義（LGBMClassifier を使用）
        model = lgb.LGBMClassifier(
            n_estimators=1000,
            learning_rate=0.05,
            num_leaves=10,#デフォルトの31から小さくし木を浅くする
            min_child_samples=30,#デフォルトの20から大きくし過学習を抑制する
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

        # 5. OOF予測（陽性クラス 1 の確率値を取得）
        val_pred = model.predict_proba(X_val)[:, 1]
        oof_preds[val_idx] = val_pred
        fold_auc = roc_auc_score(y_val, val_pred)
        print(f"Fold {fold + 1} ROC-AUC: {fold_auc:.4f}")

        models.append(model)

    # 6. 全体（Out-of-Fold）スコアの評価
    overall_auc = roc_auc_score(y, oof_preds)
    print(f"\n==============================")
    print(f"Overall OOF ROC-AUC: {overall_auc:.4f}")
    print(f"==============================")

    # 7. 分類結果の可視化
    plot_classification_results(y.values, oof_preds, threshold=0.5)


def plot_classification_results(y_true, oof_preds, threshold: float = 0.5):
    """OOF予測確率値を用いて分類結果を3面で可視化する

    Parameters
    ----------
    y_true : 1D array-like (正解ラベル 0 or 1)
    oof_preds : 1D array-like (陽性クラス 1 である予測確率)
    threshold : float (二値分類の判定閾値, default=0.5)
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # 1. 混同行列 (Confusion Matrix)
    # 指定した閾値で確率値を 0 / 1 に二値化
    y_pred_binary = (oof_preds >= threshold).astype(int)
    ConfusionMatrixDisplay.from_predictions(
        y_true,
        y_pred_binary,
        ax=axes[0],
        cmap="Blues",
        colorbar=False,
    )
    axes[0].set_title(f"Confusion Matrix (Threshold = {threshold})")

    # 2. PR曲線 (Precision-Recall Curve)
    PrecisionRecallDisplay.from_predictions(
        y_true,
        oof_preds,
        ax=axes[1],
        name="LGBM (OOF)",
        color="crimson",
    )
    axes[1].set_title("Precision-Recall Curve")
    axes[1].grid(True, linestyle="--", alpha=0.6)

    # 3. 予測確率の分布ヒストグラム (Separation Check)
    axes[2].hist(
        oof_preds[y_true == 0],
        bins=25,
        alpha=0.6,
        label="Actual Class 0",
        color="steelblue",
        density=True,
    )
    axes[2].hist(
        oof_preds[y_true == 1],
        bins=25,
        alpha=0.6,
        label="Actual Class 1",
        color="darkorange",
        density=True,
    )
    axes[2].axvline(
        threshold,
        color="black",
        linestyle="--",
        label=f"Threshold ({threshold})",
    )
    axes[2].set_title("Predicted Probability Distribution")
    axes[2].set_xlabel("Predicted Probability of Class 1")
    axes[2].set_ylabel("Density")
    axes[2].legend()
    axes[2].grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()