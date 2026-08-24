class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        [::-1]を使う？
        配列ってO(1)ではない、、、はず、、、
        [::-1]をし続けたら、逆立ちの逆立ちになって何も文字列が変わらない。
        また、ポインタ？の参照が失敗しそう。
        """
        s_reverse = []
        for i in range(1,len(s)+1):
            s_reverse.append(s[::-i])
        s = s_reverse
