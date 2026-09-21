class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        貪欲に3重ループができるか？Constraintを見ると、長さは3以上3000以下。
        3000^3=27×10^9→10^7を超えるのでTLEになる。
        numsは当然負の値が含まれる。
        逆に、2重ループなら9×10＾6でTLEにならないのか。
        setがにするのに、
        listでまずは組み合わせを全部出してから、setで括ればいいのかな？
        2個の組み合わせの和ijに対して、-ijが存在するか調べればいいのか？
        """
        reslist = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] >= 0:
                        if nums[k] <= 0 and nums[i] + nums[j] == -nums[k]:
                            reslist.append([nums[i],nums[j],nums[k]])
                    else:
                        if nums[k] > 0 and nums[i] + nums[j] == - nums[k]:
                            reslist.append([nums[i],nums[j],nums[k]])
        
        # resset = []
        # resset = set(reslist)
        return reslist
