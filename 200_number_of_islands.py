class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        dfsで隣接するセルをチェックしていく方針。
        探索完了のフラグをつけてる必要がありそう。
        未探索のうち、いずれの方向も0だったばあいに、島の数を+1する
        グリッド内、かつ未探索のノードがあ場合に処理をする
        """
        if not grid:
            return 0
        
        dx, dy = (1,1), (1,-1), (-1, 1), (-1,-1)
        def dfs(self, x :int, y:int):
            for 
