class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        直前の行と列の和が、そのグリッドへのパス数。
        num[i] = num[i] + num[i-1]（１つ上のグリッド＋１つ左のグリッド）
        空間計算量を削るために、mとnを入れかえる
        """
        # mが大きい状態を作りたい。nのほうが大きい場合は、スワップする。
        if m < n:
            m,n = n,m
        num = [1] * n

        for i in range(1,m):
            for j in range(1,n):
                num[j] = num[j] + num[j-1]
        
        return num[n-1]
