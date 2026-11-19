"""
- 文字ごとに、最後に出現した位置をメモリしておく。
- もしleftポインタよりもその位置が大きい場合は、leftポインタを移動する

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # pointers
        last_seen = dict()
        res = 0

        for right in range(len(s)):
            letter = s[right]
            if letter in last_seen and last_seen[letter] >= left:
                left = last_seen[letter] + 1
            if res < right - left + 1:
                res = right - left + 1
            last_seen[letter] = right

        return res
