class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        昇順ソート済みのnums
        ローテーションされている。
        最小値を返せ。
        時間計算量は、o(lonN）にせよ。
        通常のソートをすると、O(NlogN)かかる。
        O(logN)にするということは、
        二分探索を行い、かつ効率的に行え、ということ。

        二分探索をする中で、この異常（特定の値のみ、直後の値より小さい）
        """
