class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        # ベースルール
        if not s:
            return 0
        res = 0 # output用

        # 2番目から処理
        for i in range(0, len(s)-1):
            if values[s[i]] > values[s[i+1]]:
                res += values[s[i]]
            else:
                res -= values[s[i]]
        res += values[s[len(s)-1]]

        return res
