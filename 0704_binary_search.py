class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        数値を見つけてね。
        バイナリ探索してね。
        """
        # constraintを見るに、このベースケースは不要だが、安全のため
        if not nums:
            return -1

        # ポインタの初期化
        left = 0
        right = len(nums)-1
        mid = 0

        # 探索
        while left < right:
            mid = left + (right - left) // 2

            # 早期リターン
            if nums[mid] == target:
                return mid
            # もしmidのほうが、targetよりも大きい場合は、midを小さくしてtargetに近づける
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return mid if nums[mid] == target else -1
