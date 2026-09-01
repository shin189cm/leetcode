# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        ノードを逆に辿る。
        左の分岐から順に、逆に辿る。
        左の分岐を逆に→右の分岐を逆に→rootに戻る→右側の、左の分岐を逆に→右の分岐を逆に。
        """
        # ベースケース（終了条件）
        if not root:
            return []
        
        # 葉っぱに到達したとき
        """
        まず自分を配列に追加する。
        次に親を配列に追加する。
        次に、右の分岐があれば、右の分岐へ進む。
        もし左の分岐に進んでいれば、親の分岐は追加しない。
        
        という再帰を作る。
        """
