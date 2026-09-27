class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """
        貪欲法だ。
        後ろの空間を最大限あける。
        removeするインターバルの数を最小化する。
        逆に言えば、オーバーラップしない配列の組み合わせの個数を最大化する。
        constraint
        1 <= intervals.length <= 105
        intervals[i].length == 2
        -5 * 104 <= starti < endi <= 5 * 104
        
        105^3<10^7なので、3重ループでも大丈夫ではある。
        マイナスの値もある。

        方針
        sort()を使って、所与の配列を破壊する。endで昇順に並べる。
        intervals.sort(key=lambda x:x[1])
        順番に判定する。
        num_rem = 0
        for i in range(len(intervals)):
            if i>0 and last_end > intervals[i][0]:
                num_rem += 1

        """
        intervals.sort(key=lambda x:x[1])

        num_rem = 0
        last_end = intervals[0][1]
        for i in range(len(intervals)):
            if i>0 and last_end > intervals[i][0]:
                num_rem += 1
            else:
                last_end = intervals[i][1]
        return num_rem
