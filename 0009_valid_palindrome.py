class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        前からも、後ろからも、同じ配列
        return x == x[::-1]
        が最速だが、それ以外で得。

        右と左に分ける。
        12321
        1232,1
        123,12
        12,123
        """
        # ベースケース。そもそもマイナスはng
        if x < 0:
            return False
        if 0 <= x < 10:
            return True
        if x % 10 == 0:
            return False

        left = x
        right = 0

        while left > right:
            right = right * 10 + left % 10
            left = left // 10

        if left == right or left == right // 10:
            return True
        return False
