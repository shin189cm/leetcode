import numpy as np
import time
import matplotlib.pyplot as plt

# 初期レベル----------------------------------------------
# X = np.array([[1, 1], [1, 2], [8, 8], [9, 8], [8, 9]])
# centroids = X[[0, 1]].astype(float)   # 最初の重心

# for it in range(100):
#     # ② 各点を一番近い重心に割り当てる
#     labels = []
#     for x in X:
#         dists = []
#         for c in centroids:
#             d = np.sum((x-c)**2)
#             dists.append(d)
#         labels.append(np.argmin(dists))     # dists の中で一番小さいのは何番目？
#     labels = np.array(labels)
#     # print(labels)

#     # ③ グループごとの平均を新しい重心にする
#     new_centroids = []
#     for j in range(2):
#         points_j = X[labels==j]
#         new_centroids.append(points_j.mean(axis=0))
#     new_centroids = np.array(new_centroids)
#     print(it, labels, new_centroids)
#     if np.allclose(centroids, new_centroids):
#         break
#     centroids = new_centroids

def make_customers(seed=42):
    rng = np.random.default_rng(seed)
    # 年間購入額[万円], 月間訪問回数[回]
    centers = np.array([[ 15,  2], [ 60,  3], [ 40, 12], [110,  9]])
    stds    = np.array([[  5,  1], [ 10,  1], [  8,  2], [ 15,  2]])
    sizes   = [150, 100, 120, 80]
    X = np.vstack([rng.normal(c, s, size=(n, 2))
                   for c, s, n in zip(centers, stds, sizes)])
    y_true = np.repeat(np.arange(4), sizes)  # 答え合わせ用。学習には使わない
    return X, y_true

def kmeans(X, k, max_iter=100, seed=0):
    """
    Returns:
        centroids: (k, d)
        labels:    (n,)
        inertia:   float  # 各点から所属重心までの距離の二乗の総和
        n_iter:    int
    """
    # 重心をk個、適当に決める
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(X), size=k, replace=False)
    centroids = X[idx]

    for it in range(max_iter):
        # 各データ点を、最近傍の重心に割り当てる
        labels = []
        # for x in X:
        #     dists = []
        #     for c in centroids:
        #         d = np.sum((x-c) ** 2)
        #         dists.append(d)
        #     labels.append(np.argmin(dists))
        # labels = np.array(labels)
        
        diff = X[:, None, :] - centroids[None, :, :]
        D = np.sum(diff ** 2, axis=-1)               # diff を二乗して、最後の軸で足す
        labels = np.argmin(D, axis=1)          # 行ごとに一番小さい列の番号（前に習った関数）


        # 各グループの平均を、新しい重心にする
        new_centroids = []
        for i in range(k): # idxで回そうとしたが、ラベルが0,1,2,3しかないから、idxだと壊れるな。
            points_i = X[labels == i]
            if len(points_i) == 0:
                new_centroids.append(X[rng.integers(len(X))]) # 動かしてみる
            else:
                new_centroids.append(points_i.mean(axis=0))
        new_centroids = np.array(new_centroids)

        # 重心が変化しなくなるまで繰り返す
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    # inertiaを返す
    inertia = np.sum((X - centroids[labels]) ** 2)
    return centroids, labels, inertia, it + 1   # it は 0 から数えるので +1

def elbow(X, k_range=range(1, 11), n_init=10):
    """各kについて n_init 回実行し、最小の inertia を返す"""
    inertias = []
    for i in k_range:
        best = np.inf
        for s in range(n_init):
            _, _, inertia, _ = kmeans(X, i, seed=s)
            if best > inertia:
                best = inertia
        inertias.append(best)
    return inertias


# -------------------間数実行箇所-----------------------------------------------------
X, y_true = make_customers()
# print(kmeans(X, 4))
# t0 = time.perf_counter()
# centroids, labels, inertia, n_iter = kmeans(X, 4)
# 所属状況を確認
# for t in range(4):
#     row = np.bincount(labels[y_true == t], minlength=4)
#     print(t, " ".join([f"{v:4d}" for v in row]))
# table = np.array([np.bincount(labels[y_true == t], minlength = 4) for t in range(4)])
# print(table)
# print(inertia, n_iter)
# print(time.perf_counter() - t0, "秒")


# step2------------------------------------------------------------------------------
inertias = elbow(X)
# print(np.array(inertias).reshape(-1,1))
# plt.plot(range(1,11), inertias, marker='o')
# plt.xlabel("k"); plt.ylabel("inertia"); plt.show()

# inertias = np.array(inertias)
# rate = 1 - inertias[1:] / inertias[:-1]   # k→k+1 で何割減ったか
# for k, r in zip(range(1, 10), rate):
#     print(f"{k}→{k+1}: {r:.0%}")

# print(inertias.reshape(-1,1), np.diff(inertias).reshape(-1,1))
# max_diff_diff = -np.inf
# max_k = -1
# diff_1 = np.diff(inertias)
# diff_2 = np.diff(diff_1)
# diff_2[0] = 0

# for k,ine,d1,d2 in zip(range(1,11), inertias, diff_1, diff_2):
#     print(f"{int(k):2d}→{int(k+1):2d}, {int(ine):10d}, {int(d1):10d}, {int(d2):10d}")
#     if max_diff_diff < d2:
#         max_diff_diff = d2
#         max_k = k
# print(f"{max_k+1}になるときが、最も減少幅が大きい")
def elbow_second_diff(inertias, k_start=1):
    """二階差分が最大になる k を返す"""
    inertias = np.asarray(inertias)
    d2 = np.diff(inertias, n=2)        # n=2 で、diff を2回取ったのと同じ結果になる
    return k_start + 1 + np.argmax(d2)  # d2[j] は k = k_start + j + 1 の点の曲がり具合

# print(elbow_second_diff(inertias))

def elbow_second_diff_log(inertias, k_start=1):
    d2 = np.diff(np.log(inertias), n=2)
    return k_start + 1 + np.argmax(d2)
# print(elbow_second_diff_log(inertias))

# step3------------------------------------------------------------------------------
X_std = (X - X.mean(axis=0)) / X.std(axis=0)
inertias_raw = elbow(X)
inertias_std = elbow(X_std)

fig, axes = plt.subplots(1, 2, figsize=(10,4))
axes[0].plot(range(1,11), inertias_raw, marker='o')
axes[0].set_title("raw")

axes[1].plot(range(1,11), inertias_std, marker='o')
axes[1].set_title("std")

for ax in axes:
    ax.set_xlabel("k"); ax.set_label("inertia")
plt.tight_layout()
# plt.savefig("step3_elbow.png")
# plt.show()

print("raw", elbow_second_diff(inertias_raw))
print("std", elbow_second_diff(inertias_std))

_, labels, _, _ = kmeans(X, 4)
table = np.array([np.bincount(labels[y_true == t], minlength = 4) for t in range(4)])
print(table)

_, labels, _, _ = kmeans(X_std, 4)
table = np.array([np.bincount(labels[y_true == t], minlength = 4) for t in range(4)])
print(table)
