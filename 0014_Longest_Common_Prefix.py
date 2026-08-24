"""
Problem: 14. Longest Common Prefix (LeetCode)
URL: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Category: String / Two Pointers

Complexity:
- Time: O(S) - S は全文字列の全文字数の合計。最悪の場合すべての文字を走査
- Space: O(1) - 共通接頭辞を切り出すポインタ/インデックスのみで追加メモリ不要

Approach:
1. 入力リストが空の場合は空文字を返す
2. 基準として最初の文字列 strs[0] の各文字を先頭から順に走査する（縦走査）
3. 他の文字列で長さが足りなくなるか、文字が不一致になった時点でそこまでの文字列を返す
4. ループを完走した場合は strs[0] 全体が共通接頭辞となる
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        first_word = strs[0]
        for i, char in enumerate(first_word):
            for other_word in strs[1:]:
                if i == len(other_word) or other_word[i] != char:
                    return first_word[:i]
                    
        return first_word
