from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        ダイクストラ法を使うかと思いきや、
        重みが一様だから、BFSで解くのが最適か。
        ゴールから逆算するか？
        そのセルまで到達できる最短の経路を保存するには、どうすれば？
        1セル目はtop left
        2セル目でいける候補のうち、0をdequeに追加。
        3セル目でいける場所を、for _ in len(deque): で処理して、dequeに追加。
        4セル目でいける場所を、for _ in len(deque): で処理して、dequeに追加。
        終了条件は？
        while deque: で処理を続けて、なくなったときに判定
        visitedで訪問を取ったほうがいいかも？もしくは1に書き換えちゃうか。書き換えよう。
        もしdeque.popleft()したものが[n-1][n-1]だった場合はreturn step数
        return trueにたどり着けなったら-1を返す
        """
        if not grid:
            return -1

        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        curr_list = deque((0,0))
        curr_x,curr_y = 0,0
        direct_8 = [(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,1),(-1,0),(-1,-1)]
        steps = 1

        while curr_list:
            len_c = len(curr_list)
            for _ in range(len_c):
                curr_x, curr_y = curr_list.popleft()
                steps += 1
                for dx,dy in direct_8:
                    r,c = curr_x+dx, curr_y+dy
                if 0<=r<n and 0<=c<n and grid[r][c] == 0:
                    if r==n-1 and c==n-1:
                        return steps
                    curr_list.append((r,c))
                    grid[r][c] = 1
        return -1
