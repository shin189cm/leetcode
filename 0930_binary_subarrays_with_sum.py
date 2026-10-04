class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        prefix_sumを計算し、その差分が、走査中のnums[i]と一致するか
        配列の差ごと？にカウントを持っておく、だったかな。
        """
        if not nums:
            return 0

        n = len(nums)
        sums = [0] * n
        current_prefix_sum = 0

        for i in n:
            current_prefix_sum += nums[i]
            for j in range(0,i):
                k = current_prefix_sum - sums[j]
                if k = nums[i]:
                    sums[prefix]
