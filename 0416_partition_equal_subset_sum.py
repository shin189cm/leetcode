"""
事前にClaudeと概要会話している。
"""
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target = sum(nums) / 2
        max_num = max(nums)
        if sum(nums) % 2 != 0 or max_num > target:
            return False
        
        target = int(target)# 整数型に戻す
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
