"""Problem: 0703_kth_largest_element_in_a_stream.py

URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: Easy
Category: Heap (Priority Queue), Data Stream, Design

Complexity:
- Time:
    - __init__: O(N log k) - 初期リスト nums（長さ N）の各要素をサイズ k の最小ヒープに順次追加するため。
      （※ O(N + (N - k) log N) などのヒープ構築アプローチもあるが、O(N log k) で十分高速）
    - add: O(log k) - サイズ k のヒープに対する1回の heappush / heappop 操作に比例するため。
- Space: O(k) - ヒープ内に常に上位 k 個の要素のみを保持するため。

Approach:
1. 「k番目に大きい値」を高速に得るため、サイズ k の最小ヒープ（Min-Heap）を維持する。
2. __init__(k, nums):
    - インスタンス変数 self.k に k を保存し、self.heap を空リストとして初期化。
    - nums の各要素を add(num) を通じてヒープに追加（または全要素を heapify してから要素数が k になるまで pop）。
3. add(val):
    - ヒープに val を追加する（heapq.heappush）。
    - ヒープのサイズが k を超えた場合、最小値を1つ取り除く（heapq.heappop）。
    - これにより、ヒープ内には「これまでの全要素の中で大きい順に k 個」だけが残り、その最小値（self.heap[0]）が全体で k 番目に大きい値となる。
    - self.heap[0] を返す。

memo:
- Python の heapq は最小ヒープ（Min-Heap）のみを標準提供する。
  「最大値の上位 k 個」を求める際、サイズ k の最小ヒープを使うと根（インデックス 0）が「上位 k 個中の最小 ＝ 全体で k 番目に大きい値」となり、相性が最も良い。
- 全要素を保持してソートすると add ごとに O(M log M)（M は累積要素数）かかり、ストリーム処理ではスケールしない。
- len(self.heap) > self.k のときに pop する方針を徹底すれば、空間・時間ともに O(log k) に抑え込める。
"""

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap: List[int] = []

        # 初期データをサイズ k のヒープに流し込む
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # 新しい要素を最小ヒープに追加
        heapq.heappush(self.heap, val)

        # 要素数が k を超えたら最小値を削り、常に上位 k 個を維持
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # 最小ヒープの根（先頭）が上位 k 個の中の最小値 ＝ k 番目に大きい値
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
