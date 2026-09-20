class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        隣接する部分配列にて、合計がkと一致する配列数を返す
        開始点のポインタを持っておく
        while current_sum < k:
            current_sum += 
        """
        if not nums:
            return 0
        
        current_sum = 0
        curr_point = 0
        result = 0

        for left, num in enumerate(nums):
            current_sum = 0
            curr_point = 0
            while current_sum < k and left+curr_point < len(nums):
                current_sum += nums[left + curr_point]
                curr_point += 1
                if current_sum == k:
                    result += 1
        return result
