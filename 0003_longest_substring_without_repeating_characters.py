"""
# メモ
同じ文字を含まない文字列が、最大でどのくらいの長さになるか、答えるもの
アルファベット、数字、記号、スペースで構成されるとのこと。ざっくり300くらいか？
全部の文字用に、ハッシュマップを持っておくのも１つ。
2pointersで、出入りをチェックしていくのも手の1つ。
これでいこう。
文字列の長さは高々1万とのこと。2重ループすると1億になるので、O(N^2)だとTLEになる。

最大文字列を保管しておく話と、
現状作っている文字列を伸ばしていく話と、２つある。
max_word = 最大文字列の文字として保存
curr_word = 現状作っている文字列

curr_wordが途切れたら、、、？
先頭の文字と同じ文字に出会ったら、leftとrightをスライドする。
rightの次の文字が、現在のcurr_wordに入っているかは、set()をみないとわからん。


・ロジック
left, right = 0,0で開始する。
curr_word = set(s[0])作る。
max_word = curr_word
s[right] not in curr_wordである限り、
∟rightを1ずつ進める。
∟curr_wordを更新する。
∟max_wordとの判定をし、curr_wordのほうが長ければ書き換える
∟
…とset前提で会話していたが、setだとだめだ。leftポインタの移動が適切に行えない。


仕切り直し。
left,rightを持つ。


"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 書いていく
        if not s:
            return 0
        left, right = 0, 0
        curr_word = s[0]
        max_word = curr_word

        for i in range(1, len(s)):
            # curr_word内で一致あるかチェック
            for j in range(len(curr_word)):
                # 一致するならば、ポインタをずらす
                if s[i] == curr_word[j]:
                    left = i-len(curr_word)+j+1
                    # curr_word = s[left:i+1]
                    break
            curr_word = s[left:i+1]
            # curr_wordにs[i]が1つも一致していない場合、curr_wordを伸ばす
            if len(curr_word) > len(max_word):
                max_word = curr_word
        
        return len(max_word)
