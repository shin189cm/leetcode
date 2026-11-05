class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        複製しないこと。
        0以外の数字の、相対的な順序を保つこと。
        0を全部右寄せにすること。
        時間計算量：Ｏ（Ｎ）
        空間計算量：Ｏ（１）、なぜなら2pointerと考えたから。
        """
        # ベースケース不要。なぜならlen(nums)は1以上だから。
        left = 0
        
        # 最後に0だった場所をleftに記憶しておく。
        # 0以外を走査したとき、nums[left] = その値とする。
        # leftは、left += 1で更新する。

        for idx, num in enumerate(nums):
            if num != 0:
                # nums[left] = num
                nums[idx], nums[left] = 0, num
                left += 1
        return nums
