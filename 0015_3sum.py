class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        和が0になる、3つの整数の組み合わせを返す。
        昇順ソートする→1個目の整数を固定する→2pointersで求める和が作成できるかチェックする
        そうすると、
        時間計算量：1個目のN×Σ（N-i）なので、O（N^2）
        空間計算量：最大でNの組み合わせなので、O(N）
        """
        if not nums:
            return

        # 昇順ソート
        nums.sort()

        # 順に処理
        n = len(nums)

        for i in range(n):
            left = i + 1
            right = n - 1
            k_remain = k - nums[i]
            for j in range(i, n):
                # もしnums[0], nums[1]が同じなのは良いが、nums[2]がnums[0]と同じなのはスキップしたい
                
                while left < right:
                    if nums[left] != nums[i]
