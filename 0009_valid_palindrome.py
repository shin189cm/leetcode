"""
Problem: 9. Palindrome Number (LeetCode)
URL: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Category: Math / String

Complexity:
- Time: O(log10(N)) - 整数の桁数K（K = floor(log10(N)) + 1）に比例した文字列変換・反転・比較処理
- Space: O(log10(N)) - 桁数K分の文字列および反転文字列のメモリを確保

Approach:
1. str(x) を用いて整数を文字列に変換する
2. スライス構文 s[::-1] を使って文字列を反転させる
3. 元の文字列 s と反転文字列 s[::-1] が一致するかを比較して判定する（負の数はマイナス記号により自動的に False となる）
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
