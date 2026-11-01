from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        フレッシュオレンジが0になるまでの時間、つまり全部2になる時間
        もし不可能なら-1を返す
        そもそも1がなければ終了。
        1をまず候補として出し切る
        次に伝播させていく。     
        破壊的リプレースで、2で上書きしていく。   
        """
        if not grid:
            return -1
        
        # まず全セルを走査して、queueに2の存在するセルを入れる
        grid_r = len(grid)
        grid_c = len(grid[0])
        count_1 = 0

        queue = deque([]) # からのリストを定義する。腐敗を
        for i in range(grid_r):
            for j in range(grid_c):
                if grid[i][j] == 1:
                    count_1 += 1
                if grid[i][j] == 2:
                    queue.append((i,j)) # タプルで与える
        
        # ベースケース：そもそも1がない
        if count_1 == 0:
            return 0
        
        # 順に処理。BFS
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        steps = 0
        while queue and count_1 != 0:
            level_size = len(queue)
            for _ in range(level_size):
                # 座標を出す
                r, c = queue.popleft()
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < grid_r and 0 <= nc < grid_c and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # rottenにする
                        count_1 -= 1 # 1だった個数を1つ減らす
                        queue.append((nr,nc)) # 次の腐敗の起点としてqueueに追加する
            # おなじ層からの伝播が完了したところでステップ数を追加
            steps += 1
        # queueがなくなった時点で
        return steps if count_1 == 0 else -1
