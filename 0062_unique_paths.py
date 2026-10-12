"""Problem: 0062_unique_paths.py

URL: https://leetcode.com/problems/unique-paths/
Difficulty: Medium
Category: Dynamic Programming, Combinatorics

Complexity:
- Time: O(m * n)
    - サイズ m x n のグリッドにおける全セル (r, c) を走査する。
    - 各セルでの計算は上と左の遷移値を加算する定数時間 O(1) の操作であるため、
      全体計算量は O(m * n)。
- Space: O(min(m, n))
    - dp[r][c] の値は直前行 dp[r-1][c] と同列左 dp[r][c-1] にしか依存しない。
    - 長さ n（または min(m, n)）の1次元配列を1本保持し、左から右へ
      インプレースで加算更新していくことで空間量を O(min(m, n)) に圧縮可能。

Approach:
1. グリッドDPの定式化:
    - 各セル (r, c) に到達可能な経路数を dp[r][c] とする。
    - 各ステップで「右」または「下」にしか移動できないため、セル (r, c) に至る経路は
      「上 (r-1, c)」から下りてくるか、「左 (r, c-1)」から右に来るかの2択。
    - 漸化式: dp[r][c] = dp[r-1][c] + dp[r][c-1]
2. 空間計算量の最適化 (1D DP):
    - 1行目は右にしか進めないため、すべて 1 通り（dp 配列を 1 で初期化）。
    - 2行目以降について、各列 c (1 <= c < n) において
      `dp[c] = dp[c] + dp[c-1]` を実行する。
      右辺の `dp[c]` は更新前の値（上のセル）、`dp[c-1]` は直前に更新済みの値（左のセル）を表す。
3. 行列反転による最小化:
    - m < n の場合、行と列を反転させて走査することで、空間量を O(min(m, n)) に抑える。

memo:
- 数学的解法として、右移動 n-1 回、下移動 m-1 回の並び替え問題とみなして
  Comb(m+n-2, m-1) を O(min(m, n)) 時間・O(1) 空間で計算することも可能。
- コーディングテストでは「障害物がある場合 (LeetCode 63)」などの応用問題へ発展しやすいため、
  DPによる状態遷移の定式化と空間最適化のパターンを確実に実装できることが第一歩となる。
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 空間量を最小化するため、常に n <= m となるよう調整（n = min(m, n)）
        if m < n:
            m, n = n, m

        # dp[c] は現在行の列 c までの経路数を表す
        # 0行目はすべて 1 通りしか存在しないため 1 で初期化
        dp = [1] * n

        # 1行目から m-1 行目まで順次更新
        for _ in range(1, m):
            # 2列目を例にすると、1行上の同列の値dp[c]と、同行1列目の値dp[c-1]との和。
            for c in range(1, n):
                # 新しい dp[c] = 上のセルの値 (古い dp[c]) + 左のセルの値 (更新後の dp[c-1])
                dp[c] += dp[c - 1]

        return dp[-1]
