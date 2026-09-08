from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Problem: 0108_convert_sorted_array_to_binary_search_tree.py
URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Difficulty: Easy
Category: Tree, Binary Search Tree, Divide and Conquer, Recursion

Complexity:
- Time: O(N)
    - N は nums の要素数。
    - 全 N 個の要素についてそれぞれ 1 回ずつノード生成（TreeNode）が行われる。
    - インデックス参照のみで配列スライスを行わないため、各再帰ステップのオーバーヘッドは O(1)。
    - 合計で O(N)。
- Space: O(log N)
    - 返却する木構造そのもの（O(N)）を除いた、アルゴリズムの追加作業メモリ（再帰スタック）。
    - 常に中央値を選んで左右均等に分割するため、構築される木は完全平衡となり木の高さは O(log N)。
    - 再帰呼び出しの最大スタック深さも O(log N) となる。
    - （※ nums[:mid] などのスライスを複製する場合は O(N log N) の補助メモリを消費するが、ポインタ渡しにより O(log N) に抑制）

Approach:
1. 分割統治法（Divide and Conquer）の適用
    - 昇順ソート済み配列から左右の部分木の高さの差を 1 以下にするには、
      「中央の要素を根（ルート）として選択し、左側を左部分木、右側を右部分木にする」ことを再帰的に適用する。
2. ヘルパー関数 helper(left, right) の定義
    - ベースケース: left > right のとき、構築すべきノードは存在しないため None を返す。
    - 中央インデックスの決定: mid = (left + right) // 2
    - ルート生成: root = TreeNode(nums[mid])
    - 再帰分割:
        - root.left = helper(left, mid - 1)
        - root.right = helper(mid + 1, right)
    - root を返却する。

memo:
- 「配列スライス（nums[:mid]）」を使うとコードは短くなるが、スライスの都度リストの複製コスト O(len) が発生し
  時間計算量が O(N log N) に落ちる。インデックスポインタ（left, right）を渡すのが定石。
- 要素数が偶数の場合、(left + right) // 2 は左側寄りの中央値を選択するが、
  右側寄りの中央値を選択しても高さの差は高々 1 のままであり、どちらも LeetCode の Valid な解となる。
"""


class Solution:

  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def helper(left: int, right: int) -> Optional[TreeNode]:
      if left > right:
        return None

      mid = (left + right) // 2
      node = TreeNode(nums[mid])

      node.left = helper(left, mid - 1)
      node.right = helper(mid + 1, right)

      return node

    return helper(0, len(nums) - 1)
