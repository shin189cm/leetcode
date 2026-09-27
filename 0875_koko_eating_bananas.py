class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        バナナ食べる問題。
        もしpiles数がhを超える場合は、不可能。だがconstraintを見ると、hよりは短いので、不可能のケースはない。
        kを上から順に試していく。
        要素ごとに回数を保存する。
        その合計が余裕ある場合は、つまりsum(要素ごとの回数)<hの場合は、減らす
        whileで処理。
        piles.length<=10^4なので、O(NlogN)で処理したい。
        left, right  
        """
        # constraintからベースケースでの処理は不要
        res_k = max(piles)
        num = [1] * len(piles)

        while sum(num) < h:
            res_k -= 1
            num = [((x+res_k-1)//h) for x in piles]
        return res_k+1
