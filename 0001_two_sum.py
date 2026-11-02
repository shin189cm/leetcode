from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        diff = target - nums[i]として、keyを差分, valueをインデックスとして辞書型で持つ
        numsを走査しつつ、差分を辞書に記録していく。
        時間計算量はO(N)、空間計算量はO(N)。
        """
        seen = defaultdict()
        diff = 0

        for idx, item in enumerate(nums):
            diff = target - item
            if not diff in seen:
                seen[diff] = idx # key:value
            if item in seen:
                return [seen[item], idx]
