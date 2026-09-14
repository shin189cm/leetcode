class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        DP、2 pointersであることは、前提として知ってしまっている。
        順番にペアを作って、最大値を更新していくとみた。
        貪欲に計算したら、O(N^2)
        昇順でも降順でもないから、最後まで見ないとわからなさそう。
        最大値を保存する変数を設定。

        """
        if not height:
            return 0
        
        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                if min(height[i], height[j]) * (j-i) > res:
                    res = min(height[i], height[j]) * (j-i)
        return res
        """
        処理時間がオーバーした。
        minを計算したときに、間の数を無視できることがあるな。
        このケースだと、8と7のペアで間の6以下のheightを無視できている。
        これをするのか
        """
