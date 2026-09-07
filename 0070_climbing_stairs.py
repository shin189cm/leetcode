"""
Problem: 0070_climbing_stairs.py

URL: https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
Category: Dynamic Programming, Math

Complexity:
- Time: O(n)
    - 3 から n までの (n - 2) 回、定数時間 O(1) の加算と変数スワップのみをループ実行するため。
- Space: O(1)
    - サイズ n の DP テーブル（配列）を確保せず、直前の2状態（f(i-1), f(i-2)）を
      保持する2つのポインタ変数のみを使い回すため。

Approach:
1. 到達経路の排他分解:
    - n 段目に到達する直前の足取りは以下の2通りしか存在しない。
        1) (n - 1) 段目から 1 段登る
        2) (n - 2) 段目から 2 段登る
    - この2つの事象は「直前の位置」が異なるため完全に排他である。
    - したがって、n 段目への到達総数は f(n) = f(n - 1) + f(n - 2) となり、
      フィボナッチ数列と同一の漸化式が成立する。
2. 空間最適化 (Bottom-Up DP):
    - 通常の DP では dp = [0] * (n + 1) を確保するが、状態遷移に直前2要素しか使用しない。
    - prev2 = f(1) = 1, prev1 = f(2) = 2 と初期化し、
      現在の段数 cur = prev1 + prev2 を計算した後、
      prev2, prev1 = prev1, cur とスライド更新することで O(1) 空間を達成する。
3. エッジケース処理:
    - n <= 2 の場合は計算を走らせず、直接 n を返す。

memo:
- 制約 n >= 1 において、数学的には組合せ論 sum(_{n-k} C _k) でも解けるが、
  階乗計算やオーバーフロー/除算のオーバーヘッドを避けるため、DP が最も手堅い。
- 行列累乗法（Matrix Exponentiation）を用いれば O(log n) 時間に落とすことも可能だが、
  LeetCode 70 (n <= 45) の制約下ではループのオーバーヘッドの観点から O(n) の反復処理が最適解となる。
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1  # f(1)
        prev1 = 2  # f(2)

        for _ in range(3, n + 1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return prev1
