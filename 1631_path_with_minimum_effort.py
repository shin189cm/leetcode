"""Problem: 1631_path_with_minimum_effort.py

URL: https://leetcode.com/problems/path-with-minimum-effort/
Difficulty: Medium
Category: Graph, Shortest Path (Dijkstra), Heap (Priority Queue)

Complexity:
- Time: O(R * C * log(R * C))
    - グリッドのセル数を V = R * C とする。各セルから上下左右4方向への移動が可能なため、
      エッジ数 E は高々 4 * V。
    - ダイクストラ法において、優先度付きキュー（Min-Heap）への push/pop 操作が高々 E 回発生する。
    - 1回のヒープ操作は O(log V) なので、全体計算量は O(E log V) = O(R * C * log(R * C))。
- Space: O(R * C)
    - 各セルへの最小 effort を記録する efforts テーブルに O(R * C)。
    - ヒープ内に同時に存在する探索状態の数が最大 O(R * C)。

Approach:
1. 問題を「重み付き無向グラフにおける Minimax 最短経路問題」と捉える。
    - 各セル (r, c) を頂点、隣接セル間の標高差の絶対値 |heights[r][c] - heights[nr][nc]| をエッジの重みとする。
    - コスト関数は「経路上の全エッジの重みの最大値（Max Edge Weight）」。
2. ダイクストラ法（Dijkstra's Algorithm）による解法:
    - 通常のダイクストラ法は累積和（sum）を緩和するが、本問では「max(現在のeffort, 新しいエッジの差分)」を緩和基準とする。
    - efforts テーブルを全セル inf で初期化し、始点 efforts[0][0] = 0 とする。
    - 優先度付きキュー heap に (effort, r, c) を格納して探索を開始。
3. 枝刈りと早期終了:
    - ポップした (effort, r, c) について、effort > efforts[r][c] であれば古い探索枝としてスキップ。
    - ポップしたセルがゴール (R-1, C-1) に達した時点で、その effort が確定最小値となるため即座にリターン。

memo:
- 「4方向移動可能」「エッジの重みが非負」「ボトルネック（最大値）の最小化」という特性から、
  ダイクストラ法が最も自然かつ効率的な解法となる。
- 他のアプローチとして「答えの値を [0, 10^6] で二分探索し、到達可能性を BFS/DFS で判定する手法 (O(R * C * log(max_val)))」や、
  「エッジを差分順にソートして Kruskal 法のように Union-Find で連結判定する手法」も存在するが、
  計算量・実装量のバランスからダイクストラ法を第一選択とすべき。
"""

import heapq
from typing import List


class Solution:

  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    rows, cols = len(heights), len(heights[0])

    # 各セルへの到達に必要な最小 effort を記録
    efforts = [[float("inf")] * cols for _ in range(rows)]
    efforts[0][0] = 0

    # (effort, row, col) を格納する最小ヒープ
    heap = [(0, 0, 0)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while heap:
      current_effort, r, c = heapq.heappop(heap)

      # ゴール到達時: ダイクストラ法の性質上、最初に取り出された時点で最小値が確定
      if r == rows - 1 and c == cols - 1:
        return current_effort

      # 既により小さいコストで訪問済みの場合はスキップ
      if current_effort > efforts[r][c]:
        continue

      # 隣接4方向への遷移
      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
          # 新たな経路での effort = max(これまでの最大差分, 今回のステップ差分)
          step_cost = abs(heights[nr][nc] - heights[r][c])
          next_effort = max(current_effort, step_cost)

          # 緩和（より小さい effort で到達可能なら更新してヒープへ push）
          if next_effort < efforts[nr][nc]:
            efforts[nr][nc] = next_effort
            heapq.heappush(heap, (next_effort, nr, nc))

    return 0
