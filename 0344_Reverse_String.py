from typing import List

class Solution:

  def reverseString(self, s: List[str]) -> None:
    """Problem: 344. Reverse String

    URL: https://leetcode.com/problems/reverse-string/
    Difficulty: Easy
    Category: Two Pointers (Left & Right Pointers)

    Pattern:
    - Left & Right Pointers（両端のポインタを中央に向かって進めながら要素をスワップ）

    Complexity:
    - Time: O(N) - N / 2 回のスワップ走査
    - Space: O(1) - 追加メモリなし（in-place）

    Notes / Edge Cases:
    - 新規配列を作成して代入（s = s_reverse）してもローカル参照が変わるだけで元のオブジェクトは変更されない。
    - in-place かつ O(1) 空間制約を満たすため、直接インデックスを指定したスワップ（s[left], s[right] = s[right], s[left]）を行う。
    """    left, right = 0, len(s) - 1

    while left < right:
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1
