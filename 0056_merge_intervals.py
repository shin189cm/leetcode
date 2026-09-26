class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        オーバーラップをマージする。
        intervals.length<=10^4なので、2重ループはTLEになる。
        インプレースで破壊してよい。
        答えは出力用のlistに追加していく。

        sortする
        順番に処理する
        1つ前の要素のendと、現在の要素のstartが、end>=start の場合は、マージする。
        マージしてから、listにappendする。
        """
        if len(intervals)==0:
            return []

        intervals.sort(key=lambda x:x[0])
        res = []
        last_start = intervals[0][0]
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i-1][1] >= intervals[i][0]:
                last_end = intervals[i][1]
                res.append([last_start, intervals[i][1]])
            else:
                last_start = intervals[i][0]
                res.append([last_start, intervals[i][1]])
        return res
