"""Problem: 0643_maximum_average_subarray_i.py

URL: https://leetcode.com/problems/maximum-average-subarray-i/
Difficulty: Easy
Category: Sliding Window, Array

Complexity:
- Time: O(N) - 初期の k 要素の合計計算に O(k)、その後のスライド処理に O(N - k) かかるため全体で O(N)（N: 配列の長さ）
- Space: O(1) - 合計値を保持する定数個の変数のみを使用するため（ただし初期化時の nums[:k] は一時的に k 要素のコピーを作るため、厳密には O(k)）

Approach:
1. 先頭 k 個の要素の合計を sum(nums[:k]) で求め、window_sum および max_sum の初期値とする。
2. インデックス k から len(nums) - 1 までループを回し、ウィンドウを1要素ずつ右にスライドさせる。
3. 新しくウィンドウに入る要素 nums[i] を加算し、ウィンドウから外れる要素 nums[i - k] を減算して window_sum を差分更新する。
4. max_sum を最新の window_sum と比較して大きい方に更新する。
5. 最大合計値 max_sum を k で割った平均値を返却する。
"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k
