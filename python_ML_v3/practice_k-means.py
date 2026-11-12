import numpy as np

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
        for x in X:
            dists = []
            for c in centroids:
                d = np.sum((x-c) ** 2)
                dists.append(d)
            labels.append(np.argmin(dists))
        labels = np.array(labels)

        # 各グループの平均を、新しい重心にする
        new_centroids = []
        for i in range(k): # idxで回そうとしたが、ラベルが0,1,2,3しかないから、idxだと壊れるな。
            points_i = X[labels == i]
            new_centroids.append(points_i.mean(axis=0))
        new_centroids = np.array(new_centroids)

        # 重心が変化しなくなるまで繰り返す
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    # inertiaを返す
    inertia = np.sum((X - centroids[labels]) ** 2)
    return centroids, labels, inertia, it + 1   # it は 0 から数えるので +1

X, y_true = make_customers()
# print(kmeans(X, 4))
centroids, labels, inertia, n_iter = kmeans(X, 4)
# 所属状況を確認
# for t in range(4):
#     print(t, np.bincount(labels[y_true == t], minlength=4))

print(inertia, n_iter)
