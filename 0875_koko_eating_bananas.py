class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = 0

        while left < right:
            mid = (left + right) // 2
            res = sum([(pile + mid - 1) // mid for pile in piles])
            if res > h:# 間に合わない
                left = mid + 1
            else:
                right = mid
        return left
