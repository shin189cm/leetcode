"""
Problem: 13. Roman to Integer (LeetCode)
URL: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Category: Hash Table / Math / String

Complexity:
- Time: O(N) - 文字列の各文字を左から1回走査（制約上 N <= 15 のため実質 O(1)）
- Space: O(1) - ローマ数字7種の固定サイズ辞書と合計値変数のみ保持

Approach:
1. ローマ数字の文字と数値の対応辞書を定義する
2. 左から右へ走査し、「現在値 < 次の値」の場合は引き算、それ以外は足し算を行う
3. 最終的な total の値を返す
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)
        
        for i in range(n):
            if i + 1 < n and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
                
        return total
