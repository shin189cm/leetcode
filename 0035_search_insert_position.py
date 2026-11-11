class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        一致する要素がある場合は、その位置を返す。
        一致する要素がない場合は、インサートする場所を返す。つまり、その値以上の最小の位置を返す。lower_bound
        """
        # constraintよりif not nums:のベースケースは不要

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
