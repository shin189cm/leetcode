class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        数学的には階乗。
        整数はユニーク。
        6個だったら6重ループを回す、という話でもないし…
        再起か？
        先頭を決めると、残りで先頭を決める。残りで先頭を決める。…という方法か。
        dequeか？
        """
        if not nums:
            return [[]]
        res = []
        for i in range(len(nums)):
            queue = nums
            curr = []
            curr.append(queue.pop(i))
            while queue:
                for j in range(len(queue)):
                    curr.append(queue.pop(j))
                    while queue:
                        for k in range(len(queue)):
                            # このやり方だと、queueの中身がたりなくなる…
