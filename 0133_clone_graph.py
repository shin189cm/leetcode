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
        nodeを引数でもらう
        →[node.val, node.neighbors]として新規保存する。
        これを新規リストにappendする。
        を繰り返す。
        """
        result = []
        def dfs(node):
            result.append([node.val, node.neighbors])
        dfs(node)
