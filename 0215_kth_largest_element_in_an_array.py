"""Problem: 0215_kth_largest_element_in_an_array.py

URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
Difficulty: Medium
Category: Heap (Priority Queue), Divide and Conquer, Quickselect

Complexity:
- Time: O(N log k) - 長さ N の配列を走査し、サイズ高々 k のヒープに対して push/pop 操作（各 O(log k)）を行うため。
- Space: O(k) - ヒープ内に保持する要素数を常に最大 k 個に抑えるため。

Approach:
1. 「上から k 番目に大きい値」を求めるため、サイズ k の最小ヒープ（Min-Heap）を用意する。
2. nums 内の数値を1つずつヒープに追加（heapq.heappush）していく。
3. ヒープのサイズが k を超えたら、直ちに最小値を取り除く（heapq.heappop）。
   - これにより、ヒープ内には常に「これまで見た要素の中で大きい順に k 個」だけが生き残る。
4. 全要素の処理が終わった時点で、ヒープの根（heap[0]）には上位 k 個の中の最小値、すなわち「全体で k 番目に大きい値」が残っているため、これを返す。

memo:
- 全体をソートすると O(N log N) だが、サイズ k のヒープを使うことで O(N log k) に抑えられる（特に k << N の場合に極めて有効）。
- Python の heapq.heappushpop を使えば、サイズが k に達した後の「追加して即最小値を捨てる」処理を単一操作で高速化できる。
- 面接では別解として「Quickselect（期待計算量 O(N)）」の存在や特性（最悪計算量 O(N^2) とその回避策）について言及できると評価が高い。
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap: List[int] = []

        for num in nums:
            # ヒープのサイズが k 未満なら無条件に追加
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                # すでにサイズが k の場合：
                # 新しい要素が現在の「上位 k 個の足切りライン（min_heap[0]）」より大きい場合のみ入れ替える
                if num > min_heap[0]:
                    heapq.heappushpop(min_heap, num)

        # サイズ k の最小ヒープの根が「上位 k 個中の最小値 ＝ k 番目に大きい値」
        return min_heap[0]
