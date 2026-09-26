class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        所与のkに、合計がなる配列の個数を返す。
        constraint
        2*10^4なので、2重ループはTLEになる。10^7を超えるから。
        nums[i]がマイナスの値になる可能性もある
        つまり気を抜いていると合計になるかもしれない。
        どうやって値を持てば良いんだ・・・？
        作りまくっておけばいいのか・・・？
        dp[1]、1を作れる個数
        dp[2]、2を作れる個数（自分の直前の要素までで）
        nums[i]を最後に足したときに、kになるか
        つまり直前までの和、nums[x:i]が、
        nums[x:i]+nums[i]==kがTrueとなるか・・・
        これはバックトラック型の動的問題か。
        """
        if len(nums)==0:
            return 0

        n = len(nums)
        dp = [0] * n

        for i in range(n):
            for j in range(n-1, i-1, -1):
                if sum(nums[i:j]) + nums[j] == k:
                    dp[j] = dp[j-1] + 1

        return sum(dp)
