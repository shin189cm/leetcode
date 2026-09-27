class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        単語、作れますか？
        constraint確認。
        単語の組み合わせは無理だ。2^1000になっちゃう。
        s[:i]が作成可能かTRUE判定して、s[i:j] in wordDictがTRUEだったら、
        s[:j]が作成可能つまりTRUEとなる。
        という方法で、進める。
        """
        # 変数設定
        substr_true = [False] * (len(s)+1) # 0文字目から、n文字目まで
        substr_true[0] = True
        max_w = max(wordDict)
        
        # 処理
        for i in range(len(s)+1):
            idx_j = max(0, i-max_w)
            for j in range(i+max_w, idx_j, -1):
                if s[:i] and s[j:]
