import pandas as pd
import numpy as np
print("hello")
df_wine = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine\wine.data', header=None)
print(df_wine.head())

# データの標準化
# 共分散行列の計算
# 固有値・固有ベクトルの導出
# ソートと射影行列の構築
# データの次元削除（射影）

class ScratchPCA:
    def __init__(self, n_components: int):
        self.n_components = n_components
        self.mean_ = None
        self.components_ = None  # 射影行列 (d, k)
        self.explained_variance_ratio_ = None

    def fit(self, X: np.ndarray):
        # 1. 中心化（平均を引く）
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_

        # 2. 共分散行列の計算 (n - 1 で割る不偏共分散)
        n_samples = X.shape[0]
        cov_matrix = np.dot(X_centered.T, X_centered) / (n_samples - 1)

        # 3. 固有値分解 (エルミート/対称行列用 eigh が数値的に安定)
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

        # 4. 降順ソート
        idx = np.argsort(eigenvalues)[::-1]
        sorted_eigenvalues = eigenvalues[idx]
        sorted_eigenvectors = eigenvectors[:, idx]

        # 5. 上位 k 本の固有ベクトルを選択
        self.components_ = sorted_eigenvectors[:, :self.n_components]

        # 寄与率の計算
        self.explained_variance_ratio_ = (
            sorted_eigenvalues[:self.n_components] / np.sum(sorted_eigenvalues)
        )
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        # 学習時の平均を引いて射影
        X_centered = X - self.mean_
        return np.dot(X_centered, self.components_)

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.fit(X).transform(X)