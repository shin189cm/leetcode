# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        ▼方針
        深さ優先探索。
        5＋4＋11＋7＝22か検証する
        5＋4＋11＋2＝22か検証する
        →ここで等号が成立する。ループ終了。
        要素の探し方は、
        続く葉っぱがなくなるまで。
        今回だと、7の次はない。これは、
        1番目、2番目、4番目、8番目、16番目、と和をとっている際に、16番目がない、という状況。
        16番目がなければ、8番目で終了なので、4番目＋9番目をする。
        次が1番目＋2＋5番目。

    """
