"""
claude面接官に、事前に方針を説明済み
"""
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m :int = len(grid)
        n :int = len(grid[0])
        counts = 0
        queue : list[tuple(int)]= deque([])
        # queue = deque()
        DIRECTIONS = ((1,0),(-1,0),(0,1),(0,-1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0' # 訪問済み
                    queue.append((i,j))
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for dr, dc in DIRECTIONS:
                            nr, nc = curr_r + dr, curr_c + dc
                            if (0 <= nr < m) and (0 <= nc < n) and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                queue.append((nr, nc))
                    counts += 1
        return counts
