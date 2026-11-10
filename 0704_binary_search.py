"""Problem: 0704_binary_search.py

URL: https://leetcode.com/problems/binary-search/
Difficulty: Easy
Category: Binary Search

Complexity:
- Time: O(log N) - 各ステップで探索範囲を半分に縮小するため（N: 配列の長さ）
- Space: O(1) - ポインタ変数のみを使用し追加メモリを消費しないため

Approach:
1. 探索範囲を半開区間 [left, right) として定義（left = 0, right = len(nums)）。
   right の位置は探索範囲に含まない。
2. left < right の間ループし、中央値 mid = (left + right) // 2 を計算する。
3. nums[mid] < target なら mid 以下に答えはないため left = mid + 1 とする。
4. それ以外（nums[mid] >= target）なら mid も答え候補のため right = mid とする。
5. ループ終了時は left == right となり、left は「target 以上となる最初の位置」
   （lower_bound）を指す。
6. left が配列の範囲内かつ nums[left] == target なら left を、
   そうでなければ -1 を返却する。

Note:
- 即リターンしない lower_bound 型のため、重複がある場合も最初の位置を返す。
- ループ部分は LeetCode 35 (Search Insert Position) と共通で、
  最後の確認の有無だけが異なる。
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)  # [left, right)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if left < len(nums) and nums[left] == target:
            return left
        return -1
