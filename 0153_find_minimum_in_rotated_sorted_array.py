class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        昇順ソート配列が、右へ何個かローテーションされている。
        最小の値を返せ。
        二分探索する。
        left, right, mid=(left+right)//2

        leftは、比較対象にするとややこしい。
        もしnums[left]<nums[mid]だったら、right=mid-1
        もしnums[left]>nums[mid]だったら、left=mid。これはleftが最小値の可能性があるから。
        
        rightを、比較対象にする。
        """
        # nums.lengthは1以上なので、ベースケースは省略
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right- left)//2
            if nums[right] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]
