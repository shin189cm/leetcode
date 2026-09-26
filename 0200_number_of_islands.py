class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        島の数を数える。
        dfs
        インプレースで数え上げる。
        島の端を見つけたら、同じ島は0で書き換える。
        """
        if len(grid)==0 or len(grid[0])==0:
            return 0

        num_islands = 0
        def dfs(x :int, y:int):
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]):
                if grid[x][y] == 1:
                    grid_[x][y] = 0
                    dfs(x, y+1)
                    dfs(x, y-1)
                    dfs(x+1,y)
                    dfs(x-1.y)
                    num_islands += 1

        for i in range()
