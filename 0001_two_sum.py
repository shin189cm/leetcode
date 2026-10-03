"""
Problem: 0001_two_sum.py
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Category: Hash Table, Array

Complexity:
- Time: O(N) - 辞書へのアクセス・挿入は平均O(1)で、配列を1度走査するため
- Space: O(N) - 最大でN個の要素を辞書に格納するため

Approach:
1. 走査済みの値とそのインデックスを保持するハッシュマップ (seen) を用意する。
2. 配列を先頭から走査し、target - num (補数) が seen に存在するか確認する。
3. 存在すれば [seen[complement], i] を返し、存在しなければ現在の値とインデックスを seen に登録する。
"""

from typing import List


class Solution:

  def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
      complement = target - num
      if complement in seen:
        return [seen[complement], i]
      seen[num] = i
    return []
