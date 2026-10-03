"""Problem: 153_find_minimum_in_rotated_sorted_array.py

URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Medium
Category: Binary Search, Array

Complexity:
- Time: O(log N)
    - 探索区間 [left, right] の長さが各反復で半減する。
    - 各反復内の比較・更新処理は O(1) であり、探索は最大で ceil(log2 N) 回で終了するため全体で O(log N)。
- Space: O(1)
    - 配列内を探索するためのポインタ（left, right, mid）のみを保持するため、追加メモリは O(1)。

Approach:
1. 問題の本質（ソート済み配列の回転と単調性の崩壊）
    - 昇順ソート配列が回転された場合、配列は「左側の昇順部分」と「右側の昇順部分」の2つの部分配列に分かれる。
    - 最小値（回転の境界・変曲点）は、右側の部分配列の先頭要素である。
2. 右端要素（nums[right]）を比較基準とする二分探索
    - mid = left + (right - left) // 2 とする。
    - nums[mid] > nums[right] の場合:
        - mid は「左側の大きい方の部分配列」に属している。
        - 最小値は mid より確実に右側にあるため、left = mid + 1 とする。
    - nums[mid] <= nums[right] の場合:
        - mid は「右側の小さい方の部分配列」に属している。
        - mid 自身が最小値である可能性を含んでいるため、right = mid とする（mid - 1 にしない）。
3. 収束条件
    - left < right の間ループを回し、left == right となった時点で探索範囲が1要素に縮小され、それが最小値となる。

memo:
- 「nums[left] ではなく nums[right] と比較する」のがバグを防ぐ鍵。
    - 配列が回転されていない場合（完全な昇順の場合）、nums[mid] < nums[left] という判定は破綻するが、
      nums[right] を基準にすれば「常に右端より小さいなら左側（mid含む）へ縮退」というロジックが成立する。
- 探索区間を right = mid - 1 としない理由:
    - nums[mid] <= nums[right] のとき、nums[mid] 自体が配列全体の最小値である可能性があるため、
      探索範囲から mid を除外してはならない。
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # 最小値は mid より右側に確実に存在する
                left = mid + 1
            else:
                # 最小値は mid 自身、または mid より左側に存在する
                right = mid

        return nums[left]
