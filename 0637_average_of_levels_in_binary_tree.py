# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        さっきとほぼ同じ。
        今回は、ノード毎の値を保存する必要がある。
        """
        if not root:
            return []

        res :list[list[int]] = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                # 現在のlevelでの処理
                curr_node = queue.popleft()
                level_nodes.append(curr_node.val)

                # 子ノードの処理
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            res.append(level_nodes)
        return res
