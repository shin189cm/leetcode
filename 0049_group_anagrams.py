from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        これは特殊なやつだ。未知の体験だった。
        26文字の配列をkeyとしたdictを使って、値に各要素をappendして、dictの値だけ返すのもよいし、
        文字を1文字ずつ分解して昇順に並べなおし、それをkeyとして、判定をしてもよい。
        後者のほうがkeyがシンプルなので、後者で実装してみる。

        constraintは、strs.length、つまり所与の文字列の配列の長さが10^4なので、2重ループだとTLEになる。
        time limit error
        O(N logN）ならば、TLEにならなさそう。
        ソートの計算量がK logKだが、Kは10^2まで。
        O(N K logK)だと、10^4 * 10^2 * 2log10 < 10^7でぎりぎりおさまる
        """
        # res_dict = defaultdict(list())
        res_dict = defaultdict(list)

        # 1単語ずつ確認
        for idx, word in enumerate(strs):
            word_orgn = word
            word.sort()
            # もしソートした文字列が、辞書に含まれない場合
            if word not in res_dict:
                res_dict[word] = word_orgn
            else:
                res_dict[word].append(word_orgn)
        return res_dict
