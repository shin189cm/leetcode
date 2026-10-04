class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        constraintを確認する。
        numsが10^5なので、2重走査は間に合わない。1重で走査する。
        その場合、左右の積を保持しておき、掛ける対応をするか。
        """
        left = 1
        right = 1

        # まず1重ループで右の積の最大を作成、、、はしない。division operationが使えないから。
        
