"""Problem: 0094_binary_tree_inorder_traversal.py

URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
Difficulty: Easy
Category: Binary Tree, DFS, Tree Traversal

Complexity:
- Time: O(N) - 木のすべてのノード（N個）をちょうど1回ずつ訪問するため。
- Space: O(H) - 再帰呼び出しによるコールスタックの深さが木の高さ H に依存するため（最悪ケースの偏った木で O(N)、平衡二分木で O(log N)）。出力用リスト res は除く。

Approach:
1. 空の配列 res を用意し、ヘルパー関数 dfs(node) を定義する。
2. ベースケース: node が None（null）なら何もせずに関数を抜ける。
3. 左部分木の走査: dfs(node.left) を呼び出し、左側をすべて処理し尽くす。
4. 現在ノードの処理: node.val を res に追加する（左がすべて完了した時点で追加される）。
5. 右部分木の走査: dfs(node.right) を呼び出す。

memo:
- 再帰の仕組み: dfs(node.left) が終了して制御が戻ってきた時点が、まさに「左部分木の探索完了＝現在ノードの記録タイミング」。親に戻る処理を自前で実装する必要はない。
- Inorder の順序: [左部分木のすべて] -> [現在のノード] -> [右部分木のすべて]
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            dfs(node.left)       # 1. 左へ潜る
            res.append(node.val) # 2. 自分を記録
            dfs(node.right)      # 3. 右へ潜る

        dfs(root)
        return res
