"""Problem: 230_kth_smallest_element_in_a_bst.py

URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Difficulty: Medium
Category: Binary Search Tree (BST), Tree, Depth-First Search (Inorder)

Complexity:
- Time: O(H + k)
    - H は木の高さ（平衡木なら log N、最悪の偏った木なら N）。
    - 最小ノード（最左）に到達するまでに O(H)。
    - その後、中順走査で k 個のノードを pop して訪問するため O(k)。
    - k 番目の要素に到達した時点で探索を即時終了（Early Return）するため、
      全ノード走査 O(N) を回避できる。
- Space: O(H)
    - 明示的なスタック（stack）に格納される最大ノード数は、木の高さ H に比例する。
    - 最良・平均ケース（平衡木）では O(log N)、最悪ケース（直線状の木）では O(N)。

Approach:
1. BST（二分探索木）の重要な性質:
    - 各ノードについて「左部分木のノード値 < 自ノード値 < 右部分木のノード値」が成り立つ。
    - したがって、中順走査（Inorder: 左 -> 根 -> 右）でノードを訪問すると、
      自然に値が昇順（ソートされた状態）で取り出せる。
2. 反復法（Stack）による中順走査と早期終了:
    - 再帰を用いず、明示的なスタックを使用することで早期リターンを簡潔に実装する。
    - 現在のノードから左の子ノードを辿れるだけ辿り、スタックに push していく（最小値へ直行）。
    - これ以上左へ進めなくなったら、スタックからノードを pop して訪問（カウント k を 1 減らす）。
    - k == 0 に達したノードが「k 番目に小さい値」であるため、その値を即時 return。
    - 次に、訪問したノードの右の子へ移動し、同様の探索を繰り返す。

memo:
- 「全ノードを配列に格納して res[k-1] を返す」アプローチは実装が容易だが、
  時間計算量・空間計算量ともに O(N) となり、k が小さい場合に無駄が大きい。
- 面接では「計算量を O(H + k) に落とせるか？」「空間計算量を O(H) に抑えられるか？」
  という最適化の観点が問われるため、反復法または早期終了フラグを持つ再帰法で実装すべき。
"""

# 別解・再帰関数を使ったシンプルな実装
"""
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        def inorder(node):
            if not node:
                return []
            # 左 -> 自分 -> 右
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # 1-indexed なので k - 1 番目を取得
        return inorder(root)[k - 1]
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:

  def __init__(
      self,
      val: int = 0,
      left: Optional["TreeNode"] = None,
      right: Optional["TreeNode"] = None,
  ):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root

    while curr or stack:
      # 1. 行けるところまで左に潜る（最小値を探索）
      while curr:
        stack.append(curr) # TreeNode型のcurrがappendされている。よって後続curr.rightで右部分木も探索できる。
        curr = curr.left

      # 2. 最も左にあるノードを取り出す（昇順で次の値）
      curr = stack.pop()
      k -= 1

      # 3. k番目に到達したら探索終了
      if k == 0:
        return curr.val

      # 4. 右部分木の探索へ移行
      curr = curr.right

    return -1
