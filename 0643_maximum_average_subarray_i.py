class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        sliding windowと見た。
        最初に4つの和をとり、橋の出し入れで最大値を更新していく。
        こうすれば、時間計算量がO(N)になる。
        平均を計算するのは最後。最大値が確定してから。
        空間計算量はO(k）。
        """
        res = sum(nums[0:k])
        temp = res

        for i in range(k,len(nums)):
            temp = temp - nums[i-k] + nums[i]
            res = max(res, temp)

        return res/k
