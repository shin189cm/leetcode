# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        BSTなので、inorderに探索すると、昇順ソートした配列を順方向に走査することと同値になる。
        まずは左の部分木を全てリストに加える。
        そこでk番目の値（1-indexedなので注意）を返せれば、それで終了。
        kに到達しなかった場合は、右の部分木へ走査を進める。
        """
        # ベースケース
        if not root:
            return False
        
        min_list = []
        # まずはheapに貯める
        while root.left:
            min_list.append(root.left)
            if len(min_list) == k:
                return min_list[-1]
        
        while len(min_list) < k:
            while root.right:
                min_list.append(root.right)
                if len(min_list) == k:
                    return min_list[-1]
