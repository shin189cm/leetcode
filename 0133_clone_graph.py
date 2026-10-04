"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        参照ポインタが残らないように、インスタンスを生成するのかな。
        連結無向グラフだから、
        とにかく順番にneighborsを処理していくと、無限ループに入る可能性がある。
        よって、そのvisitedを持たせて管理することが必要。
        時間計算量は、すべてのエッジを処理するからO(E)
        空間計算量は、すべてのエッジを保持しなおすから、O(E)？
        """
        neighbors = {}
        visited = []

        curr = node
        # neighborsが残っているうちは
        while curr.neighbors and visited[curr.neighbors]:
            neighbors[curr] = curr.neighbors
            visited[curr] = True

        return list(neighbors.value())
