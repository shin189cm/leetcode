"""Problem: 994_rotting_oranges.py

URL: https://leetcode.com/problems/rotting-oranges/
Difficulty: Medium
Category: Breadth-First Search (BFS), Multi-Source BFS, Matrix

Complexity:
- Time: O(M * N)
    - グリッドのセル数を V = M * N とする。
    - 初期の走査で全セル O(M * N) を確認し、腐敗セルをキューに登録、新鮮なセル数をカウントする。
    - 各セルは最大 1 回しかキューに追加・ポップされず、各セルから 4 方向の探索を行うため、
      エッジ探索数は最大 4 * (M * N)。
    - 全体として時間計算量は O(M * N) となる。
- Space: O(M * N)
    - 入力グリッドを直接更新して訪問済みフラグ（2: 腐敗）とする場合でも、
      キュー内に同時に保持されるセル数は最大でグリッドサイズに比例するため O(M * N)。

Approach:
1. マルチソース BFS (Multi-Source BFS) の適用
    - 腐敗はすべての「初期時点で腐敗しているオレンジ（値が 2）」から同時に毎分 1 マスずつ広がる。
    - したがって、開始時にすべての腐敗オレンジの座標をキューに入れ、同時に探索を開始する。
2. 新鮮なオレンジの追跡 (fresh_count)
    - 初期化時に新鮮なオレンジ（値が 1）の総数を数えておく。
    - fresh_count == 0 の場合は、腐敗させる対象が存在しないため即座に 0 分を返す。
3. 時間（分）単位のレイヤ走査
    - 現在のキューの要素数 len(queue) 分を取り出しながら 1 分経過とする。
    - 上下左右の新鮮なオレンジを腐敗（2 に書き換え）させてキューに追加し、fresh_count をデクリメント。
    - 腐敗が実際に発生した場合のみ経過時間を +1 する。
4. 到達可能性の判定
    - キューが空になった時点で fresh_count == 0 であれば経過分数を、
      残っていれば孤立等により腐敗が全域に届かなかったため -1 を返す。

memo:
- 各ステップのコスト（時間経過）が一様（すべて 1 分）であるため、
  Dijkstra 法（O(V log V)）ではなく通常の BFS（O(V)）が時間・空間ともに最適。
- インデックスによるキュー参照ではなく、deque.popleft() による確実な要素消費を行う。
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # 初期状態の走査: 腐敗オレンジをキューへ、新鮮オレンジの数を集計
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # 新鮮なオレンジが存在しない場合は 0 分
        if fresh_count == 0:
            return 0

        minutes_elapsed = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # マルチソース BFS
        while queue and fresh_count > 0:
            # 1 分（同一レイヤ）単位でキューを走査
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # 境界内かつ新鮮なオレンジである場合のみ伝播
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))

            minutes_elapsed += 1

        return minutes_elapsed if fresh_count == 0 else -1
