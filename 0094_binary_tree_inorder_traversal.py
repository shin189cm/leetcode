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

ポイント:
- None 判定は dfs の先頭の1か所だけ。root / left / right を個別にチェックしない。
- 「左がなければ append」ではなく「左の部分木を全部見終わったら append」。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res: list[int] = []

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res

"""スタック使用版（反復版）

Complexity:
- Time: O(N) - 各ノードを1回ずつ push / pop するため。
- Space: O(H) - スタックに残るのは「左の部分木をまだ処理している途中の祖先ノード」だけで、
  その数は最大でも木の高さ H 個のため（偏った木で O(N)、平衡二分木で O(log N)）。出力用リスト res は除く。

Approach:
1. node = root から始め、左に行けるところまで行きながらスタックに積む。
2. 左に行けなくなったら、スタックから pop したノードを res に追加する。
3. そのノードの右の子に移り、1 に戻る。
4. node も stack も空になったら終了。

memo:
- 最初のメモ「左に進み続ける。左がなくなったら親→右へ進む」をそのままコードにした形。
- 再帰版で関数呼び出しが自動でやっていた「親に戻る」処理を、スタックで自前で管理している。

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res: list[int] = []
        stack: list[TreeNode] = []
        node = root
        while node or stack:
            # 左に行けるところまで行く
            while node:
                stack.append(node)
                node = node.left
            # 一番左のノードを処理して、右の部分木へ
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
"""
