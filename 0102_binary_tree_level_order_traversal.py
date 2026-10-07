# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        順方向にトラバーサルして、ノードを拾っていって、階層ごとにノードを返す。
        TreeNodeクラスがすでにある。
        constraintは、
        ノード数が2000個まで。
        値はマイナス1000からプラス1000まで。
        あー昨日のBFSをちゃんと見ておけばよかった。
        デキューするんだ。
        ノードをデキューに貯めて、
        そのデキューの長さだけ処理を回して、
        処理要素をappendしていくと同時に、
        デキューにもTreeNodeをappendしていく。
        """
        curr_nodes = deque(list(root))
        res_nodes = [[]]

        while curr_nodes:

            for _ in range(len(curr_nodes)):
                thenode = curr_nodes.popleft()
                res_nodes[-1].append(thenode)
                if thenode.left:
                    curr_nodes.deque(thenode.left)
                if thenode.right:
                    curr_nodes.deque(thenode.right)
        return res_nodes
