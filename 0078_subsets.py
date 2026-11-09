class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        バックトラック
        for i in range(len(nums)):
            # iを選ぶ場合と、選ばない場合とで、分岐したい
            選ぶ
            backtrack()する

            選ばない
            popする
            backtrack()

            こんな形だったはず。

            currを作成し、それをresにappendして、return resしたい
            

        """
        # constraintから、1 <= nums.lengthだが
        if not nums:
            return []
        
        res = []

        def backtrack():
