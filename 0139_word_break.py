class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        文字列が与えられたとき、辞書の要素の結合で文字列を作れればtrue
        辞書の要素は何回使ってもよい。

        当然、辞書の要素の全部の組み合わせを作って、sと照合すれば実行できるが、効率が悪すぎる。
        constraintを確認する。
        s.lengthは300。
        wordDict.lengthは1000。全結合作ったら、2^1000で完全にTLE
        3重ループでも10^9 > 10^7でTLE
        2重ループまで。

        catsandogの例を見ると、
        cats an dog
        cats and og
        になるが、
        これらの要素はwordDictには存在しない。

        wordDictの要素が一致する場所（インデックス）を全部返す。
        そのインデックスが、ちょうどMECEに全体を満たすものがあるか判定する。
        あればTRUE、なければFALSE
        """
