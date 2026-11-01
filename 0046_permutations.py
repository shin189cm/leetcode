class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        順番に出したり引いたり。
        計算量はlen(nums)!になりそう。
        dfsなのかな？訪問を管理する。
        queueは必要？
        毎回全部入れて、追加したらpopleft？visitedで管理しているのに？不要だろう。
        """
        if not nums:
            return

        res = [[]]
        visited = [0] * len(nums)

        while visited 
