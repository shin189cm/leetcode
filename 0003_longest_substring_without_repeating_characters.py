class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        部分文字列で、同じ文字構成が2つ以上存在する時の、最大の文字列の長さを返す。
        abcabcbbは、abcが2箇所にある。0と、3に。
        別にabcを、acb, bac, bca, cab, cbaと表現しても同じ。
        bbbbbだと、b。1文字は1つまで。
        もしsが0文字だったら、終了。len()でエラー出るから。
        まず1文字目が存在するか探す。もし見つかった場合は、2文字で一致するか探す。
        2文字の探索開始時点は、i＋1から
        """
        if not s:
            return 0
        current_str = s[0]
        max_str = current_str

        for i in range(len(s)):
            if s[0:i] in s[i:len(s)]:
                current_str = s[]
