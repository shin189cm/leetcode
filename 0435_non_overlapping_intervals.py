class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """
        被りがなくなるように削る配列が、何個か返す問題。
        つまりreturn するのはint。

        どういう方針か？
        1つ除いたら成立するか？をN個の配列に対して実施するか？
        contstraintをみる
        10^5 → 1重ループしかできない。
        またマイナスの値もある。

        1）オーバーラップしていることをどう判定するか？
        2）オーバーラップを除くときに、どうすればそれが最小削減数と見做せるか？
        
        最初にlambda x:x[0]で昇順ソートして、
        もし重複があった場合はそれを除く、というのを、順方向への1重の走査で続けるか

        idxにおいて、もしidx-1（直前）の要素のendと、自分idxのstartがend > startとなってしまった場合、
        idxを削除する。同時にnum_delete += 1
        """
        if len(intervals)==0:
            return 0
        
        intervals = intervals.sort(key=lambda x:x[0])
        num_delete = 0
        last_idx = 0

        for i in range(1, len(intervals)):
            if intervals[last_idx][1] > intervals[i][0]:
                num_delete += 1
                continue
            last_idx = i
        return num_delete
