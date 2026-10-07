"""Problem: 102_binary_tree_level_order_traversal.py

URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium
Category: Tree, Breadth-First Search (BFS), Binary Tree

Complexity:
- Time: O(N)
    - 木の総ノード数を N とする。
    - すべてのノードはキューに高々1回 push され、高々1回 popleft される。
    - 各ノードにおける子ノードの存在チェックおよび値の取得は O(1) で完了するため、
      全体の処理時間はノード数に比例して O(N) となる。
- Space: O(N)
    - キューが保持する最大要素数は、木の最大の幅（1つの階層に存在する最大ノード数）に依存する。
    - 完全二分木において最下層のノード数は高々 ceil(N / 2) となるため、キューの空間は O(N)。
    - 結果を保持する二次元リスト res に全ノードの値 N 個を格納するため、戻り値の空間も O(N)。

Approach:
1. エッジケースの処理:
    - root が None の場合は空リスト [] を即座にリターンする。
2. キューを用いた幅優先探索（BFS）:
    - collections.deque を用い、初期値として root を格納したキューを作成する。
3. 階層ごとのスナップショット走査:
    - while queue: の各反復において、現在のキューの長さ level_size = len(queue) を取得する。
    - level_size 回だけ popleft() を実行することで、現在の階層に属するノードのみを過不足なく処理できる。
    - 各ノードの val をその階層用の一時リスト level_values に追加し、左右の子ノードが存在すればキューに追加する。
    - ループ終了後、level_values を結果リスト res に追加する。

memo:
- レベル順走査（Level-order Traversal）の標準的な実装パターンであり、
  「キューの初期長さを取得してから for ループを回す」手法により、
  階層の深さを表す追加の変数をノードごとにタプルで持たせる必要がなくなる。
- 深さ優先探索（DFS: 先行順走査など）を用いて各階層の深さ (depth) を引数に渡し、
  res[depth] に追加していくアプローチでも O(N) 時間・O(H) スタック空間で解くことが可能。
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(current_level)

        return res
