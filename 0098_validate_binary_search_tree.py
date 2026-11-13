"""Problem: 0098_validate_binary_search_tree.py

URL: https://leetcode.com/problems/validate-binary-search-tree/
Difficulty: Medium
Category: Binary Tree, Binary Search Tree (BST), DFS

Complexity:
- Time: O(N) - 木の各ノード（最大 N 個）を1回ずつ訪問して値の範囲をチェックするため。
- Space: O(H) - 再帰呼び出しによるコールスタックの深さが木の高さ H に比例するため（最悪ケースで O(N)、平衡二分木で O(log N)）。

Approach:
1. ヘルパー関数 validate(node, low, high) を定義し、各ノードの値が許容範囲 (low, high) に収まっているかを検証する。
2. ベースケース: node が None なら有効な部分木とみなし True を返す。
3. 範囲判定: node.val が low 以下、または high 以上であれば BST の条件を満たさないため False を返す。
4. 再帰判定:
   - 左部分木へ進む場合: 上限を node.val に更新 (low, node.val)
   - 右部分木へ進む場合: 下限を node.val に更新 (node.val, high)
5. 左右の部分木が両方とも True であることを確認して返す。

memo:
- 「左の子 < 親 < 右の子」の局所的な比較だけでは不十分。祖先ノード全体の制約（大域的な上限・下限）を伝播させる必要がある。
  例: [5, 4, 6, null, null, 3, 7] において、3 は親 6 の左の子としては正しいが、
  根 5 の右部分木にあるため 5 より大きくなければならない。3 < 5 なので BST 違反。
- 重複値は不可（等しい値があれば BST ではない）なので、比較は狭義の < にする。
- 初期範囲は (-inf, inf) で開始する（Python では float('-inf'), float('inf') を利用）。
- 別解: 中間順（左 → 自分 → 右）にたどると BST は狭義の昇順になる。
  直前の値 prev と比べて node.val <= prev なら False を返す。
  内側の関数で prev を書き換えるので nonlocal が必要。Time O(N), Space O(H)。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # 空の部分木は条件に違反しようがないので有効
            if not node:
                return True

            # 祖先から受け継いだ範囲 (low, high) に収まっていなければ違反
            if not (low < node.val < high):
                return False

            # 左の子孫はすべて node.val 未満、右の子孫はすべて node.val より大きくなければならない
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # 根には祖先がいないので、範囲の制約はない
        return validate(root, float('-inf'), float('inf'))
