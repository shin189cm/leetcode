"""
Problem: 20. Valid Parentheses (LeetCode)
URL: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Category: Stack / String

Complexity:
- Time: O(N) - 文字列を先頭から1回走査、各 push/pop は O(1)
- Space: O(N) - すべて開き括弧の場合、最大 N 個の文字が Stack に保持される

Approach:
1. 閉じ括弧をキー、対応する開き括弧を値とするペア辞書を作成する
2. 文字列を1文字ずつ走査し、開き括弧なら Stack に push する
3. 閉じ括弧の場合、Stack が空または末尾の括弧と不一致なら False を返す
4. 走査終了後、Stack が完全に空（not stack）であれば True を返す
"""

class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        bra = {')': '(', '}':'{', ']': '['}

        if not s:
            return False

        for char in s:
            if not char in bra:
                seen.append(char)

            else:
                if not seen:
                    return False
                if bra[char] == seen[-1]:
                    seen.pop()
                else:
                    return False
        if not seen:
            return True
