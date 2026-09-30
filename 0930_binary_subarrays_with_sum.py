class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        尺取り法はできるか・・・？→できそう。負の値がないから。
        DPっぽい。
        開始からの2つの和の差をとって、
        その差がgoalと一致すれば、result += 1
        この場合、2つの配列を持つことになるので、空間計算量は多くなる。
        というか、全部保持する必要ないな。
        尺取り方でいけそう。
        むしろ、DPでやると、TLEになりそう。(3*10^4)^2=9*10^8
        """
        left, right=0,0
        n = len(nums)
        result = 0
        curr = nums[0]

        while left < n-1 or right < n-1:
            # k未満のときは、右を進める
            while curr < goal:
                right += 1
                curr += nums[right]
            while curr == goal:
                result += 1
                right += 1
                curr += nums[right]
            while curr > goal:
                if left < right:
                    curr -= nums[left]
                    left += 1
        return result
