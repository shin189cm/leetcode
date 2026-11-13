"""
二分探索木として、妥当か否か、返せ、というもの。
inorder traversalして、全部大小関係が問題ないかチェックすればいいのか。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = -2**31 - 1

        def dfs(node: TreeNode | None) -> bool:
            if not node:
                return 
            
            dfs(node.left)
            if prev < node.val:
                prev = node.val
            else:
                return False
            dfs(node.right)
        
        dfs(root)
        return True
