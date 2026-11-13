# PCA スクラッチ穴埋めドリル（分散最大化と固有値）
# ------------------------------------------------------------
# 使い方：
#   ・「# %%」ごとに1セルずつ、Jupyter か VS Code のセル実行で進めてください。
#     ______ が残っていると構文エラーになるので、1ステップずつ埋めて実行します。
#   ・各ステップの「確認」に出る値が期待どおりかを見て、次に進みます。
#   ・詰まったら「ステップ番号＋どこで止まったか」を教えてください。ヒントを段階的に出します。

# %% ステップ0：データを作る（埋める所なし）
import numpy as np

rng = np.random.default_rng(0)
n = 200
x1 = rng.normal(0, 3, n)               # 横方向に広がる変数
x2 = 0.8 * x1 + rng.normal(0, 1, n)    # x1 と強く相関する変数
X = np.column_stack([x1, x2])          # 形は (200, 2)
print("X.shape", X.shape)


# %% ステップ1：中心化して、共分散行列を自分で計算する
# 1-a: 列ごとの平均を引く（昨日のブロードキャストと同じ考え方）
Xc = X - X.mean(axis=0)

# 1-b: 共分散行列 S = (Xcの転置 @ Xc) / (n - 1)。形は (2, 2) になるはず
S = Xc.T @ Xc / (n - 1)

# 確認：np.cov と一致すれば True
print("S.shape", S.shape, np.allclose(S, np.cov(X, rowvar=False)))


# %% ステップ2：固有値分解して、第1主成分を取り出す
# 2-a: 対称行列向けの固有値分解
eigvals, eigvecs = np.linalg.eigh(S)
print("固有値:", eigvals)       # ← 並び順に注目
print("固有ベクトル:\n", np.round(eigvecs, 4))       # ← 並び順に注目。小さいほうから返してくれる！


# 2-b: 一番大きい固有値と、それに対応する固有ベクトル
#      （固有ベクトルは eigvecs の「行」と「列」のどちらに入っている？）
lam1 = eigvals[-1]
w1 = eigvecs[:,-1]

# # 確認：長さが 1 か、S @ w1 = λ1 * w1 を満たすか
print("w1:", w1, "長さ:", np.linalg.norm(w1))
print("Sw = λw ?", np.allclose(S @ w1, lam1 * w1))


# %% ステップ3：第1主成分の方向に射影して、分散を測る
# 3-a: 各サンプルを w1 の方向に射影したスコア（形は (200,) になるはず）
z1 = Xc @ w1

# 3-b: そのスコアの不偏分散（ステップ1と同じく n-1 で割る）
var_z1 = z1.var(ddof=1) # delta degrees of freedom. デルタ 自由度. 自由度がdegrees of freedom.

# 確認：var_z1 と lam1 を見比べる
print(z1.shape, "射影後の分散:", var_z1, "λ1:", lam1)
print("固有値と、射影後の不偏分散が一致するか確かめた。")


# %% ステップ4：本当に「分散が最大の方向」か、全方向を試して確かめる
# 0°〜180° を 1° 刻みで、長さ1の方向ベクトルを 181 本作る
thetas = np.linspace(0, np.pi, 181)
W = np.column_stack([np.cos(thetas), np.sin(thetas)])   # 形は (181, 2)

# 4-a: 181 方向すべてに一度に射影し、方向ごとの分散を求める
#      Xc は (200, 2)、W は (181, 2)。行列積の形を合わせるには？
proj = Xc @ W.T                         # 形は (200, 181) になるはず
variances = np.var(proj, axis=0, ddof=1)  # 形は (181,)

# 4-b: 分散が最大になった角度
best_deg = np.degrees(thetas[np.argmax(variances)])
w1_deg = np.degrees(np.arctan2(w1[1], w1[0])) % 180   # w1 の角度（向きの符号は無視）
print("全探索の最大角度:", best_deg, " w1 の角度:", w1_deg)
print("全探索の最大分散:", variances.max(), " λ1:", lam1)

# 4-c: 「長さ1」の条件を外すとどうなる？ w1 を 2 倍したベクトルで射影してみる
var_2w = (Xc @ (2 * w1)).var(ddof=1)
print("比率 = 2倍したときの分散 / λ1 =", var_2w / lam1)


# %% ステップ5：寄与率と累積寄与率
# 5-a: 固有値を大きい順に並べ替える（eigh の並び順を思い出す）
eigvals_desc = eigvals[::-1]

# 5-b: 寄与率と累積寄与率
ratio = eigvals_desc / eigvals_desc.sum()
cum_ratio = np.cumsum(ratio)
print("寄与率:", ratio, " 累積寄与率:", cum_ratio)


# %% 考察メモ（実行後に、自分の言葉で1行ずつ書いてください）
# Q-a: eigh が返す固有値はどんな順番だった？
print("昇順だった。")
# Q-b: var_z1 と λ1 の関係は？ → これが「固有値は何を表すか」の答え
print("等しい。中心化した射影ベクトルの分散と、固有値は、一致する。")
# Q-c: 4-c の結果から、「長さ1」の条件がないと何が困る？
print("分散に自由度が生まれてしまい、最適化できなくなる。")
# Q-d: w1 の符号がマイナスでも問題ないのはなぜ？
print("射影される面の形だから。")
# Q-e: 第1主成分だけで元の情報の何%を説明できた？
print("95.6%")