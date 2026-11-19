"""Problem: 0215_kth_largest_element_in_an_array.py

URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
Difficulty: Medium
Category: Heap (Priority Queue), Divide and Conquer, Quickselect

Complexity:
- Time:
    - パターンA (heapq.nlargest): O(N log k)
        - 内部でサイズ k の最小ヒープを維持し、C言語レベルで最適化された走査を行う。
    - 手動ループ (heapreplace): O(N log k) 最悪 / 最良 O(N)
        - k 番目の境界値以下の要素を O(1) で刈り取り、入替時は heapreplace で木の下り1走査のみを行う。
    - パターンB (一括 heapify + pop): O(N + (N - k) log N)
        - 全体を O(N) でヒープ化し、下位から (N - k) 回 pop する。N - k が小さい（k が N に近い）場合に有利。
- Space:
    - パターンA: O(k) - 上位 k 個の要素を保持するヒープ分の領域。
    - パターンB: O(1) - 渡された配列 nums を直接インプレースでヒープ化する場合。

Approach:
1. 「上から k 番目に大きい値」を求めるため、サイズ k の最小ヒープ（Min-Heap）を維持する。
   根（heap[0]）が常に「上位 k 個の中の最小値 ＝ 全体で k 番目に大きい値」となる。
2. アプローチの選択:
    - パターンA: Python 標準の heapq.nlargest(k, nums)[-1] を利用。
      内部でサイズ k の最小ヒープを維持しつつ、C実装による高速な走査と O(1) 足切りが行われるため最も簡潔かつ高速。
    - 手動実装: 最初の k 要素でヒープを作り、以降の要素は「num > heap[0]」のときのみ
      heapq.heapreplace(heap, num) で入れ替える。
    - パターンB: N - k << N の場合に備え、一括 heapify から不要な最小値を削り落とす解法。

memo:
- 1 <= k <= N <= 10^5 の制約において:
    - k << N（上位少数を取得）のときはパターンA / 手動ヒープ (O(N log k)) が有利。
    - N - k << N（下位少数を切り捨て）のときはパターンB (O(N + (N - k) log N)) が有利。
    - k が中央値付近 (k ≈ N / 2) の場合、ヒープ解法はいずれも O(N log N) に近づくため、
      厳密な O(N) 期待計算量を狙うなら Quickselect も有力な選択肢になる。
- 手動で上位 k 個を管理する場合、heappushpop ではなく事前に num > heap[0] を判定して
  heapreplace を呼ぶことで、余分な内部条件判定を排除し、木の走査（Sift-Down 1回のみ）を最小化できる。
- 11/19 の再挑戦: パターンB（一括 heapify + pop）で、ノーヒントAC（実装 約2分）。
    - heapify は O(N)。下の層から順に整えるので、大半を占める葉に近いノードはほとんど動かない。
      空のリストに heappush を N 回するのは O(N log N)。この2つを区別する。
    - heappop のあとの並べ直しは、木の高さぶん下がるだけなので O(log N)。O(N) ではない。
    - heapq の入れ物は普通の list（deque ではない）。heapify は list をその場で並べ替え、戻り値は None。
    - 計算量は「1要素あたり何をして、それが何回か」を先に声に出してから式にする。
- パターンB とサイズ k のヒープの比較（面接で聞かれた）:
    - ポップの回数は、どちらも N - k 回で同じ。
    - 差は「最初に入れる手間（heapify の O(N) か、push N 回の O(N log k) か）」と、
      「ポップ1回あたりの木の高さ（log N か log k か）」の2つ。
    - k が小さいと、どちらもほぼ N 回ポップするので、高さの差（log N 約17 と log k 約3）が効き、サイズ k が有利。
    - k が N に近いと、ポップは少なく、log k と log N もほぼ同じなので、
      最初に入れる手間が軽い一括 heapify が有利。
    - N = 10万（乱数）で実測: k = 10 はサイズ k 8.8ms / 一括 43.2ms、k = 9万 はサイズ k 11.4ms / 一括 7.5ms。
    - 見積の式どうしでは k = 2万前後で入れ替わるが、実測では 5万〜7万の間だった。
      乱数のデータでは heappush が平均するとほとんど上らないため、サイズ k の実際の手間は N log k より小さい。
      境界を聞かれたら「式では k = 2万前後だが、データの並び方で変わるので実測して決める」と答える。
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # -------------------------------------------------------------
        # 別解1: 手動ループによるサイズ k の最小ヒープ維持（heapreplace 版）
        # これが最も早かった
        # -------------------------------------------------------------
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        for num in nums[k:]:
            # 現在の k 番目の値より大きい場合のみ、根を上書きして Sift-Down 1回で再配置
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        
        return min_heap[0]

        
        # =================================================================
        # 模範解答: サイズ k の最小ヒープ（heappush + heappop 版）
        # Time: O(N log k) / Space: O(k)
        # 上位 k 個だけを残し、その中の最小値（根）が答え。
        # =================================================================
        # import heapq
        #
        # class Solution:
        #     def findKthLargest(self, nums: list[int], k: int) -> int:
        #         heap = []
        #         for num in nums:
        #             heapq.heappush(heap, num)
        #             if len(heap) > k:
        #                 heapq.heappop(heap)
        #         return heap[0]
        
        
        # -------------------------------------------------------------
        # パターンA: C実装の最適化を活用（最も簡潔・k << N で極めて高速）
        # 内部でサイズ k の最小ヒープを維持し、上位 k 個のリストを取得して末尾を返す
        # 遅かった。とても。
        # -------------------------------------------------------------
        # return heapq.nlargest(k, nums)[-1]


        # -------------------------------------------------------------
        # パターンB: 一括 heapify + 削り落とし（N - k << N で有利）
        # 全体を O(N) で最小ヒープ化し、小さい方から N - k 回捨てて k 番目を根に残す
        # -------------------------------------------------------------
        # heapq.heapify(nums)
        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)
        # return nums[0]
        
        
        # =================================================================
        # 参考: 私の解答（符号反転で最大ヒープ化 → k 回 pop）
        # Time: O(N + k log N) / Space: O(N)
        # 改善点: pop は k-1 回で足り、最後は nums[0] を返せば res の未定義リスクも消える。
        # =================================================================
        # import heapq
        #
        # class Solution:
        #     def findKthLargest(self, nums: list[int], k: int) -> int:
        #         nums = [-num for num in nums]
        #         heapq.heapify(nums) # time:O(N)
        #         for _ in range(k):
        #             res = heapq.heappop(nums)
        #
        #         return -res
