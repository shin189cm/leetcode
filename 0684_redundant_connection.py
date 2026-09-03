class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        無向グラフ。
        ノードがn個、エッジもn個。よって、エッジが1個あまる。よってサークルができる。
        このサークルを形成した辺、つまりサークルを完成させた辺を特定してreturnする。
        __init__
        parent
        size
        group_num

        find
        union

        親を特定するわけではない。
        サークルができあがったことを検知して、returnしたい。
        エッジを追加したときに、どっちも接続数が2以上になるとNG。どちらか片方が1である必要がある。
        """
