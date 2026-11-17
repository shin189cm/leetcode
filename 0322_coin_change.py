"""
事前に口頭説明をして、Claudeに採点してもらった。
"""
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1) # 0からamountまで作る
        dp[0] = 0 # 0円は0枚で作れるので、更新

        for coin in coins:
            for j in range(coin, amount+1):
                curr = dp[j - coin] + 1
                if dp[j] > curr:
                    dp[j] = curr
        return dp[amount] if dp[amount] < float('inf') else -1
