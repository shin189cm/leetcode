# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        """
        rootからleafまでの値の合計が、targetSumに一致するかどうか。
        1つでも和が一致するものがあればokなので、trueだったら即リターンして終了できる。

        dfsで設計したい。
        走査対象のノードを通過したとき、残りの和remain = targetSum - curr_node
        のように、値を持つ。
        """
        # ベースケース
        if not root:
            return false

        def dfs(self, node: TreeNode | None, remainSum: int) -> bool:
            # まず差分を求める
            remain = remainSum - node.val        

            # 当該ノードがleafだった場合、判定
            if not node.left and not node.right:
                return remain == 0
            
            # 次のdfsをセット
            if node.left:
                dfs(node.left, remain)
            if node.right:
                dfs(node.right, remain)

        dfs(root, targetSum)

        # もしtrueが最後まで返らなかった場合
        return false
