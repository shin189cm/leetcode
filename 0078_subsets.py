from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Problem: 0078_subsets.py

        URL: https://leetcode.com/problems/subsets/
        Difficulty: Medium
        Category: Backtracking, DFS, Recursion

        Complexity:
        - Time: O(N * 2^N) - 生成される部分集合の総数が 2^N 個あり、各部分集合を結果リストへコピーするのに O(N) かかるため（N: 配列の要素数）
        - Space: O(N) - 再帰呼び出しのコールスタックおよび探索中の一時リスト current の保持メモリ（出力用の領域を除く）

        Approach:
        1. 探索中のインデックス i を引数に取るバックトラック関数を定義する。
        2. ベースケース: i が配列の長さ len(nums) に達した時点で、現在の current のコピーを結果リストに追加して終了する。
        3. 分岐1（選ぶ）: nums[i] を current に追加し、i + 1 で次の探索を実行する。
        4. 状態の復元: current.pop() を実行して直前の状態に戻す。
        5. 分岐2（選ばない）: nums[i] を追加せずに、i + 1 で次の探索を実行する。
        """
        res = []
        current = []

        def backtrack(i: int):
            if i == len(nums):
                res.append(current[:])
                return
            
            # 分岐1: nums[i] を選ぶ
            current.append(nums[i])
            backtrack(i + 1)
            
            # 状態を巻き戻す（バックトラック）
            current.pop()
            
            # 分岐2: nums[i] を選ばない
            backtrack(i + 1)

        backtrack(0)
        return res
