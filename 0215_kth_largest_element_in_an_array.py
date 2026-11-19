import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)#return None
        while len(nums)>k:
            heapq.heappop(nums)
        return nums[0]
