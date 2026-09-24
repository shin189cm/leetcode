class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        昇順の部分配列のうち、最大長を返す。
        DPだ。
        [10,9,2,5,3,7,101,18]だったら、
        最大長のデフォルトを1おして、
        max_len = [1] * len(nums)

        idx=7の18に対して、max_len[7] = 1
        もしnum[5] < num[7]がTRUEだった場合、
        max_len[7] = max_len[5] + 1
        これは、逆順？後ろからやらず、前から考えていくと、、、
        ループ中に値が再度判定されてしまい、二度加算されてしまう、、、？
        降順で考えたいから、

        o(n^2)は避けられない・・・？
        constraintを確認すると、
        len(nums)は最大で2500。
        2重ループでも、6.25 * 10^6 < 10^7でTLEにならない。
        
        """
        max_len = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    max_len[j] = max_len[i] + 1
        return max(max_len)
