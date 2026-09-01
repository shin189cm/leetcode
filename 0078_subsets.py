class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        考えうる、全ての部分集合を返り値にするもの。
        ヒントみよう。忘れてしまった。
        選ぶ／選ばない、の再帰構造。
        popで状態の復元をするやつだ。
        """
        # ベースケース 配列が空っぽだったときに、壊れないように
        if not nums:
            return []
        
        # 出力用
        res = []

        # 配列を引数でもらったときに、整数要素を加えるか加えないかの関数
        def insert(self, arr: List[int], inte: int) -> List[int]:

        for char in nums:
            res.append(char)
            res.pop()

            res.append(char)
