# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        """
        dfsを使って、結果を作成する。
        leafノードに到達するたびに、resに追加する。
        という仕立てでコーディングする。

        def dfsの前に、
        resと、
        curr_path を宣言しておく。

        """
        # 安全のためのベースケース
        if not root:
            return 
        
        # 初期化
        res: list[str] = []
        curr_str = str(root.val)

        # 再起を作る
        def dfs(node: TreeNode) -> None:
            # 終了判定
            
            # leaf判定
            if not node.right and not node.left:
                "→".join(curr_str, str(node.val))
                res.append(curr_str)
                curr_str = str(root.val)

            # 中間ノード処理
            if node.right:
                "→".join(curr_str, str(node.val))
                dfs(node.right)
            if node.left:
                "→".join(curr_str, str(node.val))
                dfs(node.left)
        
        dfs(root)
        return res
