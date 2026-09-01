# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        二分探索木の大小関係の問題。
        左の子＜ノード＜右の子
        """
        # 親の値を覚えておく？
        par = 0

        def dfs(node: Optimal[TreeNode]) -> bool:
            # ベースケース
            if not root:
                return
            
            # 葉っぱ
            if not node.left or not node.right:
                # leftの場合、親よりも小さいとTrue
                # rightの場合、親より大きいとTrue
                par = node.val
