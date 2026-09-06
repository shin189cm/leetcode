"""Problem: 0703_kth_largest_element_in_a_stream.py

URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: Easy
Category: Heap (Priority Queue), Data Stream, Design

Complexity:
- Time:
    - __init__: O(N + (N - k) log N) - 初期リスト nums（長さ N）を一括で heapify (O(N)) し、
      サイズが k 個になるまで余分な最小値を pop ((N - k) log N) するため。
      （※ 1件ずつ add を呼ぶ O(N log k) アプローチよりオーバーヘッドが少なく高速）
    - add: 最悪 O(log k)、最良 O(1)
        - ヒープサイズ < k の場合: heappush により O(log k)
        - val > heap[0] の場合: heapreplace による木の下り走査1回のみで O(log k)
        - val <= heap[0] の場合: 既存の上位 k 個に影響しないため、ヒープ操作をスキップして O(1) で即座に返却
- Space: O(k) または O(N)
    - 初期化時に nums をそのまま参照する場合、ヒープ縮減前は O(N)、縮減後は上位 k 個のみを保持するため O(k)。

Approach:
1. 「k番目に大きい値」を高速に得るため、サイズ k の最小ヒープ（Min-Heap）を維持する。
   根（self.heap[0]）が常に「上位 k 個の中の最小値 ＝ 全体で k 番目に大きい値」となる。
2. __init__(k, nums):
    - self.heap に nums を束縛し、heapq.heapify で線形時間 O(N) でインプレースにヒープ化。
    - len(self.heap) > k の間、heapq.heappop で最小値を削り落とし、上位 k 個のみを残す。
3. add(val):
    - ヒープサイズが k 未満なら、そのまま heapq.heappush(self.heap, val)。
    - ヒープサイズが k の場合:
        - val <= self.heap[0] なら、新要素は上位 k 個に入り得ないため何もしない（O(1) スキップ）。
        - val > self.heap[0] なら、heapq.heapreplace(self.heap, val) を実行。
          （heappush + heappop のように木を往復せず、下り1走査で最小値破棄と新要素挿入を完了させる）
    - self.heap[0] を返す。

memo:
- Python の heapq は最小ヒープ（Min-Heap）のみを標準提供する。
  「上位 k 個の最大値を追跡する」タスクに対して「サイズ k の最小ヒープ」を構えると、
  最も小さい境界値（k 番目の値）が根に露出するため、極めて相性が良い。
- 1件ずつ push & pop を繰り返す素朴な実装と比較して、以下の2点で最適化している:
    1. 初期化時に関数呼び出しと逐次 push を排除し、C言語レベルで一括処理される heapify を採用。
    2. 追加値が k 番目以下のケースを O(1) で刈り取り、入替時も heapreplace で木の走査回数を半減。
"""

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # リスト全体を一括でヒープ化 (O(N))
        heapq.heapify(self.heap)

        # 要素数が k 個になるまで最小値を削り、上位 k 個のみを維持
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            # 初期要素数が k 未満のケースに対応
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            # push と pop を個別に行わず、根の置換と木の下り走査1回で済ませる
            heapq.heapreplace(self.heap, val)
        # val <= self.heap[0] の場合はヒープを更新する必要がないため O(1) で通過

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
