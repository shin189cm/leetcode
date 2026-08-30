from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """Problem: 0257_binary_tree_paths.py

        URL: https://leetcode.com/problems/binary-tree-paths/
        Difficulty: Easy
        Category: Tree/Graph, DFS/BFS, Recursion

        Complexity:
        - Time: O(N) - 木に存在するすべてのノード（N個）を1回ずつ走査するため
        - Space: O(H) - 再帰呼び出しのコールスタックの深さ。最悪ケース（直線木）で O(N)、平衡木で O(log N)（H: 木の高さ）

        Approach:
        1. 空の二分木 (root is None) の場合は空リストを返す。
        2. 再帰関数 dfs(node, path) を定義し、現在のノードとこれまでの探索経路（文字列）を引数で管理する。
        3. 葉ノード (not node.left and not node.right) に達した場合、現在のノード値を結合したパスを確定させて結果リストに追加する。
        4. 葉以外のノードでは、現在のノード値と "->" を path に追加し、左右の子ノードが存在する場合にそれぞれ再帰的に探索を実行する。
        """
        if not root:
            return []
        
        res = []

        def dfs(node: TreeNode, path: str):
            # 葉ノードに到達した時の処理
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            
            # 探索の継続（次のノードへ "->" を繋げて進む）
            if node.left:
                dfs(node.left, path + str(node.val) + "->")
            if node.right:
                dfs(node.right, path + str(node.val) + "->")

        dfs(root, "")
        return res
