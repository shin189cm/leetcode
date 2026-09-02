class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        ソートしない。
        順位キューで解く。つまりheap.
        heapq.heappush(nums, k)
        heapを使わない場合、実装する必要がある。
        """
        self.heap = nums
        return heap[k]
