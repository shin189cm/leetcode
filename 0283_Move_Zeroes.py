"""
Problem: 283. Move Zeroes
URL: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy
Category: Two Pointers (Fast & Slow Pointers)

Pattern:
- Fast & Slow Pointers（速いポインタ i が探索し、遅いポインタ idx が配置位置を管理）

Complexity:
- Time: O(N) - 配列を1周走査
- Space: O(1) - 追加メモリなし（in-place）

Notes / Edge Cases:
- 単純代入（nums[idx]=nums[i], nums[i]=0）だと、i == idx（先頭が非ゼロ）のケースで値が消失する自己破壊バグが発生する。
- 対策として要素のスワップ（入れ替え）を用いる。
"""


class Solution:

  def moveZeroes(self, nums: list[int]) -> None:
    idx = 0  # 次に「0以外の値」を配置するインデックス（遅いポインタ）

    for i in range(len(nums)):  # 探索ポインタ（速いポインタ）
      if nums[i] != 0:
        # スワップにより、i == idx の場合でも値の消失を防ぐ
        nums[idx], nums[i] = nums[i], nums[idx]
        idx += 1
