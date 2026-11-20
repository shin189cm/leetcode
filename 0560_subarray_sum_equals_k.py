class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = dict()
        counts[0] = 1 # num単独でもカウントしたい。合計0は1個作れる。
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num            
            gap = curr_sum - k
            if gap in counts:
                res += counts[gap]

            if curr_sum not in counts:
                counts[curr_sum] = 1
            else:
                counts[curr_sum] += 1

        return res


