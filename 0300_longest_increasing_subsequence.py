from typing import List

"""Problem: 0300_longest_increasing_subsequence.py

URL: https://leetcode.com/problems/longest-increasing-subsequence/
Difficulty: Medium
Category: Dynamic Programming, Binary Search (LIS)

Complexity:
- Time: O(N^2)
    - 配列長を N とする。
    - 外側ループで各要素 i（1 から N-1）を走査し、内側ループで各 i に対し
      手前のすべての要素 j（0 から i-1）を走査するため、
      比較・更新ステップ数は N * (N - 1) / 2 となり O(N^2) となる。
- Space: O(N)
    - 各要素で終わる LIS の最大長を記録する長さ N の dp 配列を保持するため。

Approach:
1. 状態の定義
    - dp[i]: nums[i] を「末尾の要素」として含む最長増加部分列（LIS）の長さ。
2. 初期化
    - どの要素単体でも長さ 1 の増加部分列を形成できるため、
      dp 配列の全要素を 1 で初期化（dp = [1] * len(nums)）。
3. 状態遷移の導出
    - 各インデックス i について、それ以前のインデックス j (0 <= j < i) を全探索する。
    - nums[i] > nums[j] の場合、nums[j] の後ろに nums[i] を連結して
      より長い増加部分列を作れる可能性があるため、以下のように更新する:
      dp[i] = max(dp[i], dp[j] + 1)
4. 解の導出
    - 最長の部分列が配列のどの要素で終わるかは事前には不明なため、
      dp 配列全体の最大値 max(dp) が全体の解となる。

memo:
- Subarray（連続部分列）ではなく Subsequence（飛び石可能な部分列）であるため、
  直前の隣接要素 nums[i-1] のみならず、過去すべての j < i を比較する必要がある。
- この O(N^2) 解法は DP の基本設計（「i番目で終わる最適な状態」を記録する）の
  典型例であり、面接での第一手として確実に実装できる必要がある。
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i] は nums[i] を末尾とする LIS の長さ
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)
