import collections
import heapq
from typing import List

"""
Problem: 0743_network_delay_time.py
URL: https://leetcode.com/problems/network-delay-time/
Difficulty: Medium
Category: Graph, Shortest Path, Heap (Priority Queue), Dijkstra

Complexity:
- Time: O(E log V)
    - V はノード数 (n)、E はエッジ数 (len(times))。
    - 隣接リストの構築に O(E)。
    - 各エッジに対してヒープへの push が最大 E 回発生し、1回の操作コストは O(log E) = O(log V)。
    - ヒープからの pop も最大 E 回発生し、各 O(log V)。
    - 全体の時間計算量は O(E log V)。
- Space: O(V + E)
    - 隣接リスト graph に O(V + E)。
    - 最短到達時間を保持する min_time 配列に O(V)。
    - ヒープ（優先度付きキュー）に最大で O(E) 個の要素が格納される。
    - 全体の空間計算量は O(V + E)。

Approach:
1. グラフの隣接リスト化
    - times の要素 (u, v, w) から、有向グラフの隣接リストを構築する。
    - 各要素は u -> [(w, v), ...] の形式（所要時間を先頭にしてヒープのキーと合わせる）。
2. 最短到達時間テーブルの初期化
    - 各ノード 1..n への最短到達時間を無限大 (float('inf')) で初期化する。
    - 始点 k への到達時間は 0 (min_time[k] = 0)。
3. 優先度付きキュー（Min-Heap）による探索
    - (累積到達時間, 現在ノード) を要素とするヒープを初期化し、(0, k) を投入。
    - ヒープから最小累積到達時間のノード (curr_time, u) を取り出す。
    - 【重要・枝刈り】取り出した curr_time が記録済みの min_time[u] より大きい場合、
      過去に確定した、より早い経路が存在するためスキップ (continue)。
    - 隣接する各ノード v について、u を経由した到達時間 (curr_time + travel_time) が
      既存の min_time[v] より小さければ、min_time[v] を更新してヒープに push。
4. 解の集計
    - すべてのノードの最短到達時間の最大値 max(min_time[1..n]) を求める。
    - 到達できないノード（値が inf のままのノード）が存在する場合は -1 を返す。

memo:
- 「全ノードにシグナルが到達する最小時間」は、各ノードへの最短到達時間の中で「最も遅いもの（最大値）」に等しい。
- 非負の重み付きグラフにおける単一始点最短経路問題であるため、ダイクストラ法が最適。
- ベルマンフォード法 O(V * E) やワーシャルフロイド法 O(V^3) でも制約 (V <= 100) 的には
  通過可能だが、実務および面接基準ではヒープを用いた O(E log V) 実装が基本形となる。
"""


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # u -> [(travel_time, v), ...]
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        # 1-indexed に合わせてサイズ n + 1 で確保
        min_time = [float("inf")] * (n + 1)
        min_time[k] = 0

        # (累積到達時間, ノード)
        pq = [(0, k)]

        while pq:
            curr_time, u = heapq.heappop(pq)

            # 確定済みの最短到達時間より大きい（古い）情報は破棄
            if curr_time > min_time[u]:
                continue

            for travel_time, v in graph[u]:
                next_time = curr_time + travel_time
                if next_time < min_time[v]:
                    min_time[v] = next_time
                    heapq.heappush(pq, (next_time, v))

        # ノード 1 から n までの最短到達時間の最大値を取得
        max_time = max(min_time[1:])

        return max_time if max_time != float("inf") else -1
