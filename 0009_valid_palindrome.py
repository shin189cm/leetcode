class Solution:
    def isPalindrome(self, x: int) -> bool:
        left, right = x, 0
        while left > right:
            amari = left % 10
            left = x // 10
            right = right * 10 + amari
        if left = right or left // 10 =right
