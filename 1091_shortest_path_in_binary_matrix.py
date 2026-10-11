"""Problem: 1091_shortest_path_in_binary_matrix.py

URL: https://leetcode.com/problems/shortest-path-in-binary-matrix/
Difficulty: Medium
Category: Graph, Breadth-First Search (BFS), Matrix / Grid

Complexity:
- Time: O(N^2)
    - グリッドのセル数を V = N^2 とする。各セルから8方向への移動が可能なため、エッジ数 E は高々 8 * N^2。
    - 訪問済みセルを即座に障害物化（1に書き換え）することで、各セルが高々1回のみキューに追加・走査される。
    - 各ステップの処理は O(1) であり、全体計算量は O(V + E) = O(N^2)。
- Space: O(N^2)
    - 最悪の場合、キュー（deque）に保持されるセル数がグリッドの全セル数に比例するため O(N^2)。
    - grid を直接訪問済みフラグとして再利用するため、追加の visited 配列は不要。

Approach:
1. 重みが一様な最短経路問題:
    - すべてのエッジの移動コストが 1 であるため、ダイクストラ法ではなく BFS が最適（O(V + E)）。
2. コーナーケースの除外:
    - 始点 (0, 0) または終点 (N-1, N-1) が 1（障害物）の場合は到達不能のため即座に -1 を返す。
    - N = 1 かつ grid[0][0] == 0 の場合は、始点＝終点であるため 1 を返す。
3. BFS 探索とインプレース訪問管理:
    - (r, c, dist) を要素とするキューを用意し、始点 (0, 0, 1) をエンキュー。
    - 重複探索を防ぐため、エンキューした時点で grid[0][0] = 1 に変更。
    - 8方向の遷移先 (nr, nc) が範囲内かつ値が 0 であれば、終点到達判定を行い、未到達ならエンキューして grid[nr][nc] = 1 とする。
"""

from collections import deque
from typing import List


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 始点または終点がブロックされている場合は到達不可能
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # 始点がそのままゴールの場合 (1x1 グリッド)
        if n == 1:
            return 1
        
        # (row, col, distance)
        # deque((0, 0))とすると、要素が2つに分裂してしまう
        # distはタプルに持たせる。多重ループでのミスを防げるから。各ノードが自立的にdistを保持できるから。
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1  # 訪問済みとしてマーク

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    # ゴールに到達した時点で最短距離が確定
                    if nr == n - 1 and nc == n - 1:
                        return dist + 1

                    grid[nr][nc] = 1  # キューに追加する時点で訪問済みにする
                    queue.append((nr, nc, dist + 1))

        return -1
