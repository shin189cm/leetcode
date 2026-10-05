"""
Problem: 637_average_of_levels_in_binary_tree.py
URL: https://leetcode.com/problems/average-of-levels-in-binary-tree/
Difficulty: Easy
Category: Tree, Breadth-First Search (BFS), Depth-First Search (DFS)

Complexity:
- Time: O(N)
    - N は二分木に含まれる総ノード数
    - 各ノードはキューに高々1回 push され、1回 pop される
    - 各ノードに対する子の参照や加算処理は O(1) で完了するため、全体で O(N)
- Space: O(M)
    - M は木の中で最もノード数が多い階層の幅（Max Width）
    - キューに同時に格納されるノード数の最大値に依存する
    - 完全二分木の場合、最下層の葉ノード数は最大約 N/2 となるため最悪空間計算量は O(N)
    - 平均的な平衡二分木でも O(N) となる

Approach:
1. 木の階層別走査（Level-order Traversal）に BFS を採用
    - FIFO（先入れ先出し）データ構造である collections.deque をキューとして使用する
2. 階層ごとの区切り判定
    - 外側の while ループでキューが空になるまで探索を継続する
    - 各階層の処理開始時点での queue の長さ（level_size = len(queue)）を取得する
    - この level_size 回だけ内側の for ループを回すことで、同一階層のノードのみを正確に処理する
3. 平均値の算出と次階層のキューイング
    - 内側ループ内で各ノードの val を合計（level_sum）に加算する
    - 左右の子ノードが存在すればキューの末尾に追加する
    - 内側ループ終了後に level_sum / level_size を算出し、結果リストに追加する

memo:
- Python のリスト (`list.pop(0)`) は要素のシフトが発生し O(K) かかるため、
  BFS のキューには必ず両端 O(1) で操作可能な `collections.deque` を使用すること
- DFS でも深さ（depth）を引数に持たせて各深さごとの合計と個数を管理することで同等計算量で解くことが可能だが、
  本問のように階層ごとの集約を行う問題では BFS の方が直感的かつ状態管理が簡潔になる
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if not root:
            return []

        result: list[float] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result
