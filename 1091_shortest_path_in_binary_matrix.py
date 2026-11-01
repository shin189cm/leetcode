from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        0を通過して、pathを作る。
        隣接セルは、斜めも含める。
        通過するセル数を返す。
        もし不可能だったら,1を返す。
        →スタートが1 or ゴールが1の場合、return -1
        
        ダイクストラ法は、コストがエッジごとに異なる場合に使用する。
        このケースだと、BFSで管理できそう。
        最終、grid[n-1][n-1]に到達したことにすればよい。
        隣接するセルをqueueに追加して、
        層別に処理していくか。
        最終的に、popleftしたセルの座標が、[n-1][n-1]であればいい。
        """
        if not grid:
            return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        cells :int = 1
        queue = deque([(0,0)])
        DIRECTIONS = (
            (-1,1), (0,1), (1,1), 
            (-1,0), (1,0), 
            (-1,-1), (0,-1), (1,-1), 
        )

        while queue:
            level_size = len(queue)
            cells += 1
            for _ in range(level_size):
                curr_grid = queue.popleft()
                r,c = curr_grid
                for dr,dc in DIRECTIONS:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0:
                        if nr == n-1 and nc == n-1:
                            return cells
                        queue.append((nr, nc))
        return -1
