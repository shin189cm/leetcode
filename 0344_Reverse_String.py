class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        while left < len(s)/2:
            s[left], s[-(left+1)] = s[-(left+1)], s[left]
            left += 1
