from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Problem: 0035_search_insert_position.py

        URL: https://leetcode.com/problems/search-insert-position/
        Difficulty: Easy
        Category: Binary Search

        Complexity:
        - Time: O(log N) - 各ステップで探索範囲を半分に縮小するため（N: 配列の要素数）
        - Space: O(1) - 定数個のポインタ変数のみを使用するため

        Approach:
        1. 探索範囲を閉区間 [left, right] として設定する（left = 0, right = len(nums) - 1）。
        2. left <= right の間、中央値 mid を算出して二分探索を実行する。
        3. nums[mid] == target なら mid を返却する。
        4. nums[mid] > target なら target は左半分にあるため right = mid - 1 とする。
        5. nums[mid] < target なら target は右半分にあるため left = mid + 1 とする。
        6. target が存在しないまま探索を終えた場合、ループ終了時点で left は「target 以上の最小要素のインデックス（＝挿入位置）」を指しているため、left を返却する。
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left
