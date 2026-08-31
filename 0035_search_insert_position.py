class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        左右にポインタを設定し、大小関係で判定し、探索エリアを絞る。
        二分探索の基本形。
        """
        # ポインタ
        left, right = 0, len(nums)-1

        # 処理
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
