class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        要素数kのサブ配列のうち、平均が最大のものの平均値を返す問題。
        再計算を省略する。
        """
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, current_sum)
        return max_sum / k
