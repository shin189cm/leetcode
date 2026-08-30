# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Problem: 0112_path_sum.py

        URL: https://leetcode.com/problems/path-sum/
        Difficulty: Easy
        Category: Binary Tree, DFS, Recursion

        Complexity:
        - Time: O(N) - 全てのノードを最大1回走査するため（N: ノード数）
        - Space: O(H) - 再帰呼び出しのコールスタックの深さ。最悪ケース（直線状の木）で O(N)、平衡木で O(log N)（H: 木の高さ）

        Approach:
        1. 空ノード (root is None) の場合はパスが存在しないため False を返却する。
        2. 葉ノード（左右の子ノードが共に None）に到達した際、ノードの値が残りの targetSum と一致するかを判定する。
        3. 葉以外のノードでは、現在のノード値を targetSum から減算し、左右の部分木に対して再帰的に探索を実行する。
        4. 左右いずれかのパスで合計が一致すればよいため、論理和 (or) の結果を返却する。
        """
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(
            root.right, remaining
        )
