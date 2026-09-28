class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        アナグラムだ。2pointersかしら。違うか。
        回答は、2次元配列に文字列を含めてreturnする。
        constraint
        strsは1以上10^4以下。
        strsの要素の長さは、0以上100以下。
        strsの要素はアルファベットの小文字。
        2重ループはTLEになる。
        O(NlogN)はTLEにならない。

        案1：1文字ずつにして、set作る？これは無理そう。
        案2：順方向に1重走査。文字数でsortして、同じ文字数同士で比較。
        しかしここで2重ループになってしまうので、これを工夫して防ぐ。
        文字数ぶんO(1)で保持して、順走査していく？
        毎回先頭の文字を分解してset()しハッシュ化して、文字数ぶん走査する。
        eatを、set([e,a,t])して、 for str in strs: while str[i] in set([e,a,t]): 
        もしFALSEになった場合は、新しく保存しておく。
        TRUEのままstrが終了した場合は、appendする。
        """
        result = [[""]]
        strs.sort(key=lambda x:len(x) for x in strs)
