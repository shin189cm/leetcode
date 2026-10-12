class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        代数的に考えると、m+nのうちn個を選ぶパターン数だな。        
        """
        # まず1つ先のgrid[0][1]と、grid[1][0]はパターンは1のみ。
        # 次にgrid[a][b]は、grid[a-1][b]+grid[a][b-1]のパターン数。
        # ただしa-1 やb-1が0未満の場合は、0となる。
        
