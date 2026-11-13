"""
ストリーム。k番目までの応募者をリアルタイムで残す。

"""
from collections import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = heapq(nums, k)
                

    def add(self, val: int) -> int:
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
