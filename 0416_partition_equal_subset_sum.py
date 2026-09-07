class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        配列を2分割して、合計値が等しくなるようにできる場合はTrueを返せ。
        全部試すと、大量の計算量になる。
        全体の和に対して、その半分の値になるか。
        """
        # そもそも合計値が奇数だったら弾く
        if sum(nums) % 2 == 1:
            return False
        
        half = sum(nums) // 2

        # コイン問題とは異なるが、合計値を求める
        
