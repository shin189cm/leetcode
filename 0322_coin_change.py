class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        与えられたコインを使い、最小枚数で、与えられたamountを計算せよ。
        そのときの最小枚数をreturnせよ。
        ただしぴったり構成できない場合は、-1をreturnせよ。
        組み合わせでやりたいが、できないか・・・？
        通常の思考法だと、
        まず値の大きいコインでぎりぎりまでアプローチ
        あまりがあれば、2番目に大きいコインで余りを求める。
        全てのコインを試して、あまりが0にならなければ、
        値の大きいコインの使用枚数を1枚減らして試す。
        最大枚数で繰り返し構文か。
        coins.sort()
        coin_num = list[]
        for i in range:
            coin_1st: int = amount // coins

        max_coin = max(coins)
        remain = amount // max_coin
        if remain == 0:

        """
