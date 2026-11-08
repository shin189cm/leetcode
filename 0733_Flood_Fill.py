from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        """
        sr,sc,color
        開始セルが与えられる
        隣接する、縦横の最大4セルを走査する
        開始セルと同じ色のセルならば、指定のcolorに色を塗り替える
        隣接セルに、開始セルと同じ色のセルがなくなり塗ることができなくなったら、終了。
        そもそも、開始セルが、塗る色と一致していた場合は、即終了。

        処理は、最大でm x n x 4なので、時間計算量はO(m x n)
        空間計算量は

        bfsで管理するのが何となく自然。
        一方で、層管理は不要だから、Dfsで素直に探していっても解けそう。
        bfsで管理して、空間計算量を節約しよう。

        隣接するセルをdequeオブジェクトのquueに追加
        """
        if not image:
            return
        # 即終了
        if image[sr][sc] == color:
            return image
        
        queue = deque([sr, sc, image[sr][sc]])
        m = len(image)
        n = len(image[0])
        DIRECTIONS = (
            (1,0),(-1,0),(0,1), (0,-1)
        )
        

        # 塗り替え可能なセルが存在する限り
        while queue:
            # 既存のセルの処理
            curr = queue.popleft()
            c, r, c_color = curr
            # 塗り替える
            image[c][r] = color

            # 次のセルの追加
            for dr,dc in DIRECTIONS:
                nr,nc = c+dc, r+dr
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] != color:
                    queue.append([nr, nc, image[nr][nc]])
        # リターン
        return image
