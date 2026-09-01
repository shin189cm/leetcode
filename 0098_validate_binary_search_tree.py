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
  例: [5, 4, 6, null, null, 3, 7] において、3 は親 6 より小さいが、根 5 より小さいため BST 違反。
- 初期範囲は (-inf, inf) で開始する（Python では float('-inf'), float('inf') を利用）。
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       # 【ステップ1】関数の定義（設計図を作るだけ。この時点では中身は動かない）
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # 空ノードは有効な BST
            if not node:
                return True

            # 現在のノードが許容区間 (low, high) に収まっているか確認
            if not (low < node.val < high):
                return False

            # 左に進むときは上限を node.val に狭め、右に進むときは下限を node.val に狭める
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
           
        # 【ステップ2】ここで初めて実行開始！
        # root を渡し、範囲を (-∞, +∞) に設定して最初の1回目をキックする
        return validate(root, float('-inf'), float('inf'))
