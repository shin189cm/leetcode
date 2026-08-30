class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        numsは昇順。
        targetをnumsの中から探す。
        もし存在する→インデックスを返す。
        もし存在しない→-1を返す。
        時間計算量はO(logN)しか許されない。
        バイナリリサーチ。
        """
        # ベース条件
        if not nums:
            return -1

        # ポインタ設定
        left, right = 0, len(nums)-1

        # 繰り返し
        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid
            elif num[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            if left == right:
                return -1
