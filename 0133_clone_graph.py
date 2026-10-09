"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: 'Node | None') -> Optional['Node']:
        """
        複製する。
        単なるポインタの複製にならないようにする。
        無向グラフの無限ループにならないようにする。

        # 1つずつqueueに加えて、処理していくのかな
        queue = node.neighbors
        
        # クラスを使ってインスタンスを生成する。ここに複製していく。
        result = Node()

        # neightborsが残っているうちは
        while queue:
            # まずloopの回数を確保
            n = len(queue)
            # 各neighborsにおいて
            for i in range(n):
                # Nodeクラスのインスタンスを生成して、resultの要素に追加したい
                curr = Node()
        """        
        # ベースケース
        if not node:
            return []
        
        result  = Node(node)
        next_node = node.neighbors

        while next_node:
            curr = Node(next_node)
            next_node = 
