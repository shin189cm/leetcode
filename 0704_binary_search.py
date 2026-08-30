from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Problem: 0704_binary_search.py

        URL: https://leetcode.com/problems/binary-search/
        Difficulty: Easy
        Category: Binary Search

        Complexity:
        - Time: O(log N) - 各ステップで探索範囲を半分に縮小するため（N: 配列の長さ）
        - Space: O(1) - ポインタ変数のみを使用し追加メモリを消費しないため

        Approach:
        1. 探索範囲を閉区間 [left, right] として定義（left = 0, right = len(nums) - 1）。
        2. left <= right の間ループし、中央値 mid = left + (right - left) // 2 を計算する。
        3. nums[mid] == target なら mid を返却する。
        4. nums[mid] > target なら target は左半分にあるため right = mid - 1 とする。
        5. nums[mid] < target なら target は右半分にあるため left = mid + 1 とする。
        6. ループを抜けても見つからなかった場合は -1 を返却する。
        """
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
