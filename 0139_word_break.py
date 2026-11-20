"""
もしsが、スペースで分割して、wordDictの要素に分解できるなら、Trueを返す。
sの長さは、1以上300以下。
wordDictの要素数は、1以上1000以下。
wordDictの要素の長さは、1以上20以下。
SもwordDictの要素も、小文字だけ。
wordDictの要素は、ユニーク。

sのi文字目までは作成できます、というのを、dp[i]で表現する。
dp[0]はTrue。
sの1文字ずつ、ループで進めていく。
もしdp[i]がTrue and s[i:i+j] in wordDictもTrue であれば、dp[i+j]はTrueになる。
※wordDictは集合にしたほうが検索しやすそう
最終的なreturnは、dp[n], nはlen(s)

iとjの動かし方を決めたい。
外側ループがi、内側でjとしてwordDictの要素の最大長として回すと、
300×20×1000=6,000,000 < 10^7
ギリギリ間に合いそう。

"""
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        max_word = max(len(word) for word in wordDict)
        word_dict = set(wordDict)
        dp = [False] * (n + 1) # 0-indexed
        dp[0] = True # 0文字目までは作成できるからTrue

        for i in range(n+1):
            for j in range(1, max_word+1):
                if i + j < n + 1 and dp[i] and s[i:i+j] in word_dict:
                    dp[i+j] = True
        return dp[n]
