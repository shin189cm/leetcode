import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# print("hello")
df_wine = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine\wine.data', header=None)
# print(df_wine.head())

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

# xyへの代入
X = df_wine.iloc[:,1:].values
Y = df_wine.iloc[:,0].values

# 分割
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42)

# 前処理
sc =StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

# モデルの実行
n_components = 5

# scratchPCA
scratch_pca = ScratchPCA(n_components=n_components)
X_train_scratch = scratch_pca.fit_transform(X_train_std)
X_test_scratch = scratch_pca.fit_transform(X_test_std)

# sklearnPCA
sklearn_pca = PCA(n_components=n_components)
X_train_sklearn = sklearn_pca.fit_transform(X_train_std)
X_test_sklearn = sklearn_pca.fit_transform(X_test_std)

# 検証
assert np.allclose(
    scratch_pca.explained_variance_ratio_,
    sklearn_pca.explained_variance_ratio_,
    atol=1e-5
), "寄与率が一致しません"
print(f"チェック　寄与率の検証：ok {scratch_pca.explained_variance_ratio_}")

assert np.allclose(
    np.abs(X_train_scratch),
    np.abs(X_train_sklearn),
    atol=1e-5
), "Trainデータの変換結果が一致しません"
print(f'訓練データの射影検証：ok.')

assert np.allclose(
    np.abs(X_test_scratch),
    np.abs(X_test_sklearn),
    atol=1e-5
), "Testデータの変換結果が一致しません"
print(f'訓練データの射影検証：ok.')

identity_check = np.dot(scratch_pca.components_.T, scratch_pca.components_)
assert np.allclose(
    identity_check, np.eye(n_components), atol=1e-5
), "固有ベクトルが直交していません"
print(f'固有ベクトルの正規直交性検証：ok\n{identity_check}')

print('\n全テスト通過：ScratchPCAの実装は数学的・使用的に正常です')