# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        TreeNodeクラスが宣言されている。要注意。
        ルートに戻ってきたら、終了。
        再帰関数使う。
        もし葉ではなかったら、継続処理。”自分→”をappendする。      
        もし葉で、次のleftもrightもなかったら、"自分”をappendする。TRUEを返す。
        """
        output = ""
        part = []

        # 最初にルートノードの判定

        # 次に葉ではないノードの判定
        if not (self.left) and not(self.right):
            output.append(self.val, "→")
            return FALSE
        
        # 葉での処理
        if self.left == None:
            output.append(self.val)
            part.append(output)
            self.binaryTreePath(root)
        if self.right == None:
            output.append(self.val)
            part.append(output)
            self.binaryTreePath(root)
