"""
二分探索木のバリデーション。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None, min: float, max: float) -> bool:
            # leftやrightに進んだが、ノードが存在しなかった場合
            if not node:
                return True
            
            # 値がmin
            if not (min < node.val < max):
                return False
            
            return dfs(node.left, -float('inf'), node.right.val) and dfs(node.right, node.val, float('inf'))
        
        dfs(root, -float('inf'), float('inf'))
