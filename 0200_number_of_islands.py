from collections import deque
from typing import List

"""
Problem: 0200_number_of_islands.py
URL: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Category: Graph, Breadth-First Search (BFS), Depth-First Search (DFS), Matrix

Complexity:
- Time: O(M * N)
    - M をグリッドの行数、N を列数とする。
    - 外側の二重ループで、全セルを1回ずつ見る（M * N 回）。
    - 中に while ループがあるが、各セルはキューに入れる時点で '0' に書き換えるため、
      1つのセルがキューに入るのは、すべての島を合計しても最大1回。
      よって while ループの中身が実行される回数は、全体で M * N 回以下。
      （三重ループに見えるが、O((M * N)^2) にはならない）
    - 1回ごとの処理（4方向の確認、書き換え、append）は O(1)。
    - 合計すると、外側のループで M * N、BFS で最大 4 * M * N となり、O(M * N)。
- Space: O(min(M, N))
    - 入力の grid を書き換えて訪問済みにするため、訪問済みを覚えるメモリは不要。
    - 追加で使うのは BFS のキューのみ。全部陸のグリッドで左上から BFS を始めると、
      キューに同時に入るのは、始点から同じ距離にあるセル（斜めの線の上に並ぶセル）だけ。
      その長さは短いほうの辺を超えないため、O(min(M, N))。
    - 島の形によってはこれより多くなる場合もある。上限は O(M * N)。

Approach:
1. 左上から順に全セルを見る。
    - まだ '0' にしていない '1' を見つけたら、新しい島とみなしてカウントを +1 する。
2. 見つけたセルを始点に BFS を行い、同じ島の陸をすべて '0' に書き換える。
    - 始点は、キューに入れる時点で '0' にする。
    - キューから取り出したセルの上下左右を確認し、グリッドの内側で、かつ '1' なら、
      '0' に書き換えてからキューに入れる（同じセルが二度キューに入るのを防ぐ）。
3. すべてのセルを見終わったら、カウントを返す。

memo:
- 事前に方針を口頭で説明し、Claude に採点してもらった上で実装したコード（模擬ライブコーディング）。
- grid の値は文字列の '0' / '1'。整数の 0 / 1 と比べると、条件が常に False になる。
- DFS ではなく BFS を選ぶ理由:
    - Python の再帰の上限は、初期設定で 1000。
    - 全部陸の 300 * 300 のグリッドを再帰の DFS で探索すると、深さが最大 9万になり、
      RecursionError で落ちる可能性がある。
    - BFS（または、スタックを使った再帰なしの DFS）なら、この問題は起きない。
    - 再帰の DFS の空間計算量は、コールスタックの深さで決まり、最悪 O(M * N)。
- 面接では、入力を書き換えてよいかを最初に面接官に確認する。
- 入力を書き換えられない場合（下の numIslands_visited を参照）:
    - visited = [[False] * n for _ in range(m)] で、訪問済みを記録する2次元リストを作る。
    - [[False] * n] * m と書くと、同じ1行を m 回参照するリストになる。
      1つのセルを書き換えると、同じ列の全部の行が変わってしまうので使わない。
    - grid をコピーして書き換える場合は、[row[:] for row in grid] のように行ごとにコピーする。
      grid.copy() や grid[:] では、中の各行が元の grid と共有されたままになる。
    - 空間計算量は、visited に M * N 個必要になるため、O(min(M, N)) から O(M * N) に増える。
      時間計算量は O(M * N) のまま変わらない。
- visited は、集合 set() でも書けるが、大きさが決まったグリッドでは2次元リストのほうがよい。
    - 判定はどちらも O(1)（集合は平均 O(1)、最悪 O(N)）。
    - 集合は、判定のたびにタプル (r, c) を作り、ハッシュ値を計算するので遅い。
    - 300 * 300 で判定 100万回を実測すると、2次元リスト 約0.05秒、集合 約0.13秒（約2.5倍）。
      全セル訪問済みのときのメモリは、2次元リスト 約0.74MB、集合 約9.2MB（約12倍）。
    - 集合が向いているのは、訪問するセルが全体のごく一部の場合や、座標の範囲が決まっていない場合。
- 型ヒントを書くなら、キューは deque[tuple[int, int]]。中身と合わない型ヒントは付けない。
- Union-Find でも解ける（隣り合う '1' どうしを union し、最後に根の数を数える）。
"""


class Solution:
    DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0
        queue: deque[tuple[int, int]] = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue

                # まだ '0' にしていない '1' を見つけたら、新しい島
                island_count += 1
                grid[i][j] = "0"  # キューに入れる時点で訪問済みにする
                queue.append((i, j))

                # 同じ島の陸をすべて '0' に書き換える
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in self.DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"  # 二重にキューに入らないよう、入れる前に書き換える
                            queue.append((nr, nc))

        return island_count

    def numIslands_visited(self, grid: List[List[str]]) -> int:
        """別解：入力の grid を書き換えられない場合。空間計算量は O(M * N)。"""
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]  # 行ごとに別のリストを作る
        island_count = 0
        queue: deque[tuple[int, int]] = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1" or visited[i][j]:
                    continue

                island_count += 1
                visited[i][j] = True
                queue.append((i, j))

                while queue:
                    r, c = queue.popleft()
                    for dr, dc in self.DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < m
                            and 0 <= nc < n
                            and grid[nr][nc] == "1"
                            and not visited[nr][nc]
                        ):
                            visited[nr][nc] = True
                            queue.append((nr, nc))

        return island_count
