"""
Problem: 0322_coin_change.py
URL: https://leetcode.com/problems/coin-change/
Difficulty: Medium
Category: Dynamic Programming, Breadth-First Search

Complexity:
- Time: O(S * n)
    - S は amount の値、n は coins の要素数（種類数）。
    - 0 から amount までの各金額（S + 1 状態）に対して、利用可能な全コイン（n 種類）を
      1回ずつ走査して遷移を行うため、全体のループ回数は S * n 回となる。
- Space: O(S)
    - 0 から amount までの各金額を作るための最小枚数を保持する配列 dp のサイズが S + 1。
    - 入力以外の追加メモリはこれのみであるため O(S)。

Approach:
1. 貪欲法（大きい硬貨から優先して使う）は反例（例: coins=[1,3,4], amount=6 で 4+1+1=3枚 vs 3+3=2枚）
   が存在するため使用不可。部分問題の重複構造を活かす動的計画法（Bottom-up DP）を採用する。
2. dp[i] を「金額 i を構成するのに必要な最小コイン枚数」と定義する。
    - ベースケース: dp[0] = 0（金額0は0枚で達成可能）
    - 未到達状態の初期化: amount より絶対に大きくならない上限値として float('inf')
      （または amount + 1）で埋める。
3. 遷移式:
    - 1 から amount までの各金額 i について、各コイン c を試す。
    - i - c >= 0 かつ dp[i - c] が到達可能であれば、
      dp[i] = min(dp[i], dp[i - c] + 1)
4. 最終結果:
    - dp[amount] が初期値のままであれば構成不能なため -1 を返す。
    - 更新されていれば dp[amount] を返す。

memo:
- 「ナップサック問題（個数無制限＝完全ナップサック）」の最小化版と同型。
- BFS（幅優先探索）でも解くことが可能。キューに (現在の合計金額, 現在の枚数) を入れ、
  visited で到達済み金額を枝刈りすれば、最初に amount に到達した瞬間が最小枚数となる。
  平均的には BFS の方がターゲット金額へ早く辿り着いて early-stopping できる場合もあるが、
  DP の方が配列のみで完結しオーバーヘッドが少ない。
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] は金額 i を構成するための最小コイン数
        # amount を超える枚数には絶対になり得ないため、番兵として amount + 1 を使用
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1
