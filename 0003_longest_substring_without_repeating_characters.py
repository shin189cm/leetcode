class Solution:
    """
    Problem: 0003_longest_substring_without_repeating_characters.py
    URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Difficulty: Medium
    Category: Hash Table, String, Sliding Window

    Complexity:
    - Time: O(N) - 文字列を1回走査し、各文字のハッシュマップ参照・更新はO(1)で行えるため
    - Space: O(min(N, M)) - 文字列長Nまたは文字セットサイズM（ASCIIなら最大128など）のハッシュマップを使用するため

    Approach:
    1. 各文字の直近の出現インデックスを保持するハッシュマップ (char_index_map) と、ウィンドウの左端 (left) を用意する。
    2. 文字列を先頭から right ポインタで走査する。
    3. 現在の文字が char_index_map に存在し、かつそのインデックスが left 以上であれば、left を「前回の出現位置 + 1」にジャンプさせる。
    4. 現在の文字のインデックスを更新し、現在のウィンドウ幅 (right - left + 1) で max_len を更新する。
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_len = 0
        left = 0

        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
