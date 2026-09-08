# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        サブツリーの高さが等しくなる？
        最大でも1ちがいにして！という問題。
        dpの問題なんだろう。
        BSTを作成するときって、
        大小関係を保持しつつ、深さも調整していくのか。
        1。midをバイナリサーチで特定
        2。その上下で分類？
        3。
        """
