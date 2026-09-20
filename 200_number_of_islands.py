from typing import List

"""Problem: 200_number_of_islands.py

URL: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Category: Graph, Depth-First Search (DFS), Breadth-First Search (BFS), Matrix

Complexity:
- Time: O(M * N)
    - M をグリッドの行数、N を列数とする（全セル数 V = M * N）。
    - グリッドの走査で全セルを1度確認し、各陸地セルに対する DFS 探索も高々1回しか実行されない。
    - 各セルから上下左右4方向への分岐処理は定数時間 O(1) で行われるため、
      全体の計算量はセル数に比例する O(M * N) となる。
- Space: O(M * N)
    - 訪問済みフラグとして入力 grid をインプレースで '0' に書き換えるため、
      追加の訪問管理テーブル用メモリは O(1)。
    - 一方で、グリッド全体が陸地で構成されるような最悪ケースにおいて、
      DFS の再帰呼び出しスタックの深さが最大で M * N に達するため、
      コールスタックによる空間計算量は O(M * N) となる。

Approach:
1. グリッド全体の走査と島の検知
    - 行 r（0 から M-1）および列 c（0 から N-1）の二重ループで走査する。
    - grid[r][c] == '1'（未訪問の陸地）を発見した場合、新しい島を発見したとみなし
      島の総数カウントを +1 する。
2. DFS による連結成分の訪問済み化（Sink 処理）
    - 発見したセルを起点として DFS を呼び出し、上下左右に隣接するすべての陸地を探索する。
    - 再帰先が以下のいずれかを満たす場合は探索を終了（枝刈り）する:
        a. グリッド範囲外（r < 0 or r >= M or c < 0 or c >= N）
        b. 水域、またはすでに訪問済みのセル（grid[r][c] == '0'）
    - 条件を満たす陸地セルは即座に grid[r][c] = '0' に上書きして訪問済みにする。
    - 上下左右の4方向 `(r+1, c), (r-1, c), (r, c+1), (r, c-1)` に対し再帰的に DFS を実行する。

memo:
- グリッドのグラフ問題における連結成分（Connected Components）を数え上げる基本問題。
- 再帰上限（Python のデフォルトは約 1,000）を超える可能性がある規模の入力に対しては、
  `collections.deque` を用いた BFS、または明示的なスタックを用いたイテレーティブな DFS で
  書き換えることで、スタックオーバーフローのリスクを回避できる。
- 探索方向のベクトルは `directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]` のように
  リスト化してループ処理すると、コードの冗長化を防ぎバグを減らしやすい。
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r: int, c: int) -> None:
            # 範囲外または水域/訪問済みの場合は即終了
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            # 現在の陸地セルを訪問済みにマーク（沈める）
            grid[r][c] = "0"
            
            # 上下左右の4方向を探索
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c)
                    
        return island_count
