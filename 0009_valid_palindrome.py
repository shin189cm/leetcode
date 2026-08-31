class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        left, right = x, 0
        while left > right:
            amari = left % 10
            left = left // 10
            right = right * 10 + amari

        return left == right or left == right // 10
