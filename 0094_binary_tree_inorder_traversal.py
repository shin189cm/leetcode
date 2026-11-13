"""
inorder traversalか。
ベースケースは、return []

左に進み続ける。
leftがなくなったら、親→右→と進む。
左があれば、左に進み続ける。
dfsでかけそう。
時間計算量は、O(N)か。ノード数だけ。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # ベースケース
        if not root:
            return []
        
        # 変数の初期化
        res: list[int] = []

        # dfs定義
        def dfs(node: TreeNode | None) -> None:
            # もし左があれば、左に進む
            if node.left:
                dfs(node.left)
            # もし左がなければ、自分のvalをappendする
            # else:
            #     res.append(node.val)
            
            # 親として
            res.append(node.val)

            # もし右があれば、
            if node.right:
                dfs(node.right)
        
        # 実行
        dfs(root)

        return res
