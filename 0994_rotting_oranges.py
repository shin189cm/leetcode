class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        DPに見えなくもないが、BFSなんだろうな。
        ダイクストラ法でもできそう。
        どっちのほうが計算量少ないんだろう？

        constraint
        grid, grid[i],それぞれ1以上、10以下。
        （1）queueに隣接するセルを追加する
        （2）queue内部のセルの状態を、値が1の場合のみ更新していき、
        同時に1の場合はqueueにそのセルを追加する
        （3）上の（1）（2）を繰り返す
        （4）
        これ最後にどうやって終了した判定を返すんだ？

        queueがなくなったら終了して、ステップ数をreturnか
        ステップ数をカウントしておく必要がある。
        """
        # ベースケースは不要。グリッドが存在するconstraintだから。
        if not grid:
            return 0

        # 変数の宣言
        queue = deque([])
        cnt_step = 0
        m = len(grid)
        n = len(grid[0])

        # 初めに、腐っているセルを全部見つける必要があるか
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])

        while queue:
            for i in range(len(queue)):
                r, c = queue[i][0], queue[i][1]
                # queueに入っているセルの、上下左右の座標の値を処理する
                for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                    # もし調査範囲が範囲内で、
                    if 0 <= r + dx < m and 0 <= c + dy < n:
                        # もし中身が1だった場合、2にする
                        if grid[r+dx][c+dy] == 1:
                            grid[r+dx][c+dy] = 2
                            queue.append([r+dx, c+dy])
                        # もし中身が0か2だった場合、continue
                        if grid[r+dx][c+dy] == 0 or grid[r+dx][c+dy] == 2:
                            continue
            cnt_step += 1
        return cnt_step
