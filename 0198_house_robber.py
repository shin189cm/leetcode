"""
問いの確認。
建物を１つとばしで盗む。
ハウスごとの盗める金額がnums。
盗む金額を最大化したい。
dpで比較と思われる。

制約の確認。
numsの長さは、1以上、100以下。
numsの要素の値は、0以上、400以下。

進め方
dp配列で、その家までで盗み切ったときの最大金額を管理する。
つまり初期値は0でおいておく。
0-indexedで考える。
dp[0] = nums[0]
dp[1] = nums[1]
dp[2] = max(dp[1], dp[0]+nums[2]) # nums[2]の家から盗まないほうが高いか否か
return dp[len(nums)]

と思ったが、dpで持たなくてもよい。直前2か所までの家の値のみ保持できればok
修正する。
dp_last_2  = nums[0]
dp_last_1  = nums[1]
dp[i] = max(dp_last_1, dp_last_2 + nums[i]) # nums[i]の家から盗まないほうが高いか否か

"""
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        dp_last_2  = nums[0]
        dp_last_1  = max(nums[0], nums[1])
        dp_curr = 0

        for i in range(2, n):
            dp_curr = max(dp_last_1, dp_last_2 + nums[i]) # nums[i]の家から盗まないほうが高いか否か
            dp_last_2 = dp_last_1
            dp_last_1 = dp_curr
        return dp_curr
