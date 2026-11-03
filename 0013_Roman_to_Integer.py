class Solution:
    def romanToInt(self, s: str) -> int:
        """
        もし次の要素と比較して、大きい場合は、加算する
        小さい場合は、減算する
        最後の要素は、必ず足す
        """
        dic={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        n = len(s)
        res = 0
        for i in range(n-1):
            if dic[s[i]] >= dic[s[i+1]]:
                res += dic[s[i]]
            else:
                res -= dic[s[i]]
        res += dic[s[n-1]]
        return res
