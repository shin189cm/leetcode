class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        整数配列が与えられたとき、昇順になっていている部分配列のうち、
        最も長いものの長さを返す。
        """
        max_len = 1
        current = 1
        curr_list = []

        for i, num in enumerate(nums):
            if i + 1 < len(nums):
                if num < nums[i+1]:
                    current += 1
                    curr_list.append(num)
                    if current > max_len:
                        max_len = current
                else:
                    currnet = 0
                    curr_list = []
        return curr_list
