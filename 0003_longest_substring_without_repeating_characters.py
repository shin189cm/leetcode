"""
Problem: 0003_longest_substring_without_repeating_characters.py
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Category: Hash Table, String, Sliding Window

Complexity:
- Time: O(N) - 文字列を1回走査し、各文字のハッシュマップ参照・更新はO(1)で行えるため
- Space: O(min(N, M)) - 文字列長Nまたは文字セットサイズM（ASCIIなら最大128など）のハッシュマップを使用するため

Approach:
1. 各文字の直近の出現インデックスを保持するハッシュマップ (last) と、ウィンドウの左端 (left) を用意する。
2. 文字列を先頭から right ポインタで走査する。
3. 現在の文字 c が last に存在し、かつそのインデックスが left 以上であれば、left を「前回の出現位置 + 1」にジャンプさせる。
4. c の出現位置を更新し、現在のウィンドウ幅 (right - left + 1) で best を更新する。

Pattern (スライディングウィンドウの型):
    right を1つ進める
    → 条件を満たさなくなったら、満たすまで left を進める
    → 答えを更新する

- set 版: while で left を1つずつ進める（位置情報がないため）
- dict 版: 最後の出現位置がわかるので、if で left を一気にジャンプさせる
- 注意: dict は left より前の古い位置も残るため、last[c] >= left の条件が必須
  （例: "abba" で最後の 'a' を見るとき、left が後ろに戻ってしまう）
- 類題: LC 76, 159, 209, 424

Reflection:
- 方針（2ポインタ＋set）は早く立てられたが、「left をどう動かすか」で詰まった（40分でAC）
"""
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}   # 文字 -> 最後に出現した位置
        left = 0
        best = 0

        for right, c in enumerate(s):
            # ウィンドウ内に重複があれば、left をその次へジャンプ
            if c in last and last[c] >= left:
                left = last[c] + 1

            # 出現位置を更新し、最大長を更新（重複の有無にかかわらず毎回実行）
            last[c] = right
            best = max(best, right - left + 1)

        return best
