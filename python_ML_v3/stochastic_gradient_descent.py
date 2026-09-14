import numpy as np
from numpy.random import seed
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class AdalineSGD(object):

    def __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None):
        # インスタンス生成時に、どんな属性名でアクセスできるか決める。設定される属性値も決める。
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized = False
        self.shuffle = shuffle
        self.random_state = random_state
        
    def fit(self, X, y):
        self._initialize_weights(X.shape[1])
        self.cost_ = [] # 末尾がアンダースコアなのは、フィッティング後に動的に生成される属性のため。つまり計算結果が入る場所。
        
        for i in range(self.n_iter):
            
            # 最適化計算が2回目以降の場合、訓練データの反復のたびに、重みベクトルが同じ値に戻ってしまわないように
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = [] # 通常の変数
            
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost) / len(y)
            self.cost_.append(avg_cost)
        return self # メソッドチェーン、つまり処理の連続実行ができる。戻り値に対して、どっと記法で続けて別のメソッドを呼び出せる。機械学習あるある。
        
    # オンライン学習用。つまり、新しい訓練データが届いた際に、その場でモデルを訓練するもの。streamの状況で有用。
    def partial_fit(self, X, y):
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, y)
        else:
            self._update_weights(X, y)
        return self
        
    # 学習データが固定された順序で循環することによるリミットサイクルを防ぐ
    def _shuffle(self, X, y):
        r = self.rgen.permutation(len(y))
        return X[r], y[r]
        
    # パーセプトロンの場合は、重みをわずかに0からずらして初期化する必要あり。
    # そうしないと、学習率イータが、重みベクトルの向きと大きさのうち、大きさにしか影響しなくなってしまう。
    # ADALINEの場合は、0初期化でok。目的関数が二乗誤差和で凸関数だから。
    def _initialize_weights(self, m):
        self.rgen = np.random.default_rng(self.random_state)
        self.w_ = self.rgen.normal(loc=0, scale=0.01, size=1 + m)
        self.w_initialized = True
        
    # xiごとに、係数のw_iを更新する
    def _update_weights(self, xi, target):
        output = self.activation(self.net_input(xi))
        error = target - output
        self.w_[1:] += self.eta * xi.dot(error) # x_1からx_mまでの係数を算出。m+1の大きさの1次元配列の、idx=1からidx=mまでの部分配列。 
        self.w_[0] += self.eta * error # 定数部分の値を算出。m+1の大きさの配列の初項。
        cost = 0.5 * error**2 # 誤差平方和
        return cost
    
    # 総入力（重みつき総和＋バイアス）の計算。活性化関数に通す前の、正味の値だから、netという名前。
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0] # 要素数nの、1次元配列が返される
        
    # ロジスティック回帰などの場合、ここで数値処理が入る。ｍ
    def activation(self, z):
        return z
    
    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1) # 要素数nの、1次元配列が返る
        
# 分類を描画する関数
def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('s', 'x', 'o', '^', 'v')
    colors=('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:,0].min() - 1, X[:, 0].max() + 1    
    x2_min, x2_max = X[:,1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.xlim(xx2.min(), xx2.max())
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')

# 読み込み
df = pd.read_csv('iris_data',
                 header=None,
                 encoding='utf-8')

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0,2]].values

# 標準化
X_std = np.copy(X)
X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

# 最適化
ada_sgd = AdalineSGD(n_iter=15, eta=0.01, random_state=1)
ada_sgd.fit(X_std, y)

# 描画
plot_decision_regions(X_std, y, classifier=ada_sgd)
plt.title('Adaline - Stochastic Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

plt.plot(range(1, len(ada_sgd.cost_) + 1), ada_sgd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Average Cost')

plt.tight_layout()
plt.show()

# ada_sgd.partial_fit(X_std[0, :], y[0])
"""
このコードは『Python機械学習プログラミング』の2章後半で登場する確率的勾配降下法（SGD：Stochastic Gradient Descent）を用いた AdalineSGD の実装の一部である。
ここには、通常の勾配降下法（バッチ勾配降下法）とは根本的に異なる重要なロジックが含まれている。

以下の3点において、論理的な挙動を整理する。

1. 「xiごとに重みを出して」の厳密な意味
単に計算して出力しているのではなく、データ1件（`xi`）ごとに重みパラメータをその都度「更新（上書き）」している。
`_update_weights(xi, target)` の内部では、以下の3つの処理が逐次実行されている。

1. `xi` を用いて予測値を出し、`target` との誤差を計算する。
2. その1件の誤差だけを使って、即座にモデルの重み（`self.w_`）を更新する。
3. その1件に対するコスト（通常は誤差の二乗の1/2）を計算して `return` する。

2. n回分のループ処理が意味するもの（バッチGDとの比較）
通常の勾配降下法（AdalineGD）では、$n$ 行すべてのデータから誤差の総和を計算し、ループを抜けた後に「1エポックあたり1回」だけ重みを更新する。
しかし、提示された SGD の実装では、1エポックの中で $n$ 回、重みが少しずつ変更され続けている。
つまり、1行目の `xi` と n 行目の `xi` を処理する時点では、使われている重みが異なっている。

3. cost（平均誤差）の計算の性質
ループ内で `cost.append(...)` されている値は、「その時点での重みを使って発生した、各データ点における個別のコスト」の集まりである。
ループ終了後の以下のコード：

```python
avg_cost = sum(cost) / len(y)
self.cost_.append(avg_cost)

```

これは、1エポック（データ全体を1周）する間に発生した各データのコストの平均値を求め、学習の収束具合を確認するための履歴（`self.cost_`）として保存している。

結論
「1件ごとに処理を行い、$n$ 行全部終わった後にターゲットとの平均誤差を計算（記録）している」という理解で正しいが、
最大のポイントは「誤差の計算だけでなく、ループを回す1行ごとにモデル（重み）が学習・変化しながら進んでいる」という動的なプロセスにある。
"""