# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        再帰的に行う。
        右rightを開け続けて計算する。
        """
        node = root[0]

        # ベースルール
        if not root:
            return False
        
        if node.left  and node.right:
            return targetSum == node.val

        targetSum = targetSum - node.val
                
        if not node.left or not node.right:
            return self.hasPathSum(self, targetSum)
