"""
Problem: 13. Roman to Integer (LeetCode)
URL: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Category: Hash Table / Math / String

Complexity:
- Time: O(N) - 文字列の各文字を左から1回走査（制約上 N <= 15 のため実質 O(1)）
- Space: O(1) - ローマ数字7種の固定サイズ辞書と合計値変数のみ保持

Approach:
1. ローマ数字の文字と数値の対応辞書をクラス定数として定義する
2. 左から右へ走査し、「次の文字が存在し、かつ現在値 < 次の値」の場合は引き算、それ以外（現在値 >= 次の値、または末尾文字）は足し算を行う
3. 最終的な total の値を返す
"""

class Solution:
    ROMAN_MAP = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        total = 0
        n = len(s)

        for i in range(n):
            current_val = self.ROMAN_MAP[s[i]]
            if i + 1 < n and current_val < self.ROMAN_MAP[s[i + 1]]:
                total -= current_val
            else:
                total += current_val

        return total

# 逆走査
"""
class Solution:
    ROMAN_MAP = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        res = 0
        prev_val = 0
        
        # 右から左へ走査
        for char in reversed(s):
            val = self.ROMAN_MAP[char]
            if val < prev_val:
                res -= val
            else:
                res += val
            prev_val = val
            
        return res
"""
