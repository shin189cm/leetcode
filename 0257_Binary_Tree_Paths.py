# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        方針：再帰
        ベースケース（除外上限）
        葉っぱでの処理
        葉っぱ以外での処理

        ベースケース：if not root: return []
        葉っぱでの処理:if not node.left and node.right:
        valを追加する

        葉っぱ以外での処理
        valと->を追加する

        悩み：nodeってどうやって宣言するか
        """
        def dfs(self, node: Optional[TreeNode]):
            # ベースケース
            if not root:
                return []
            
            # 変数
            curr_item = ""
            res = []

            # 葉っぱでの処理
            if not node.left and node.right:
                curr_item.append(node.val)

            # 葉っぱ以外での処理
            if node.left or node.right:
                curr_item.append("->", node.val)
                return dfs(node.left) or dfs(node.right)
            
            res.append[curr_item]
        
        dfs(root)
        return res
