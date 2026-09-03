from typing import List


class UnionFind:

  def __init__(self, n: int):
    self.parent = list(range(n))
    self.size = [1] * n
    self.group_count = n

  def find(self, x: int) -> int:
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])  # 経路圧縮
    return self.parent[x]

  def union(self, x: int, y: int) -> bool:
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x == root_y:
      return False

    # Union by Size: 小さい木を大きい木の下に統合
    if self.size[root_x] < self.size[root_y]:
      root_x, root_y = root_y, root_x

    self.parent[root_y] = root_x
    self.size[root_x] += self.size[root_y]
    self.group_count -= 1
    return True


class Solution:

  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    """Problem: 0547_number_of_provinces.py

    URL: https://leetcode.com/problems/number-of-provinces/
    Difficulty: Medium
    Category: Graph, Disjoint Set (Union-Find), Depth-First Search,
    Breadth-First Search

    Complexity:
    - Time: O(N^2 * alpha(N)) - 隣接行列の全要素（N * (N - 1) / 2 ペア）を走査し、各ペアに対してほぼ定数時間 alpha(N) で Union 操作を実行するため。実質 O(N^2)（N: 都市の数）
    - Space: O(N) - Union-Find 内部で各頂点の親 (parent) と木のサイズ (size) を保持するためにサイズ N の配列を確保するため

    Approach:
    1. 都市数 N 個の要素を管理する Union-Find データ構造を初期化する。初期のグループ総数は N とする。
    2. 隣接行列 isConnected の上三角部分 (i < j) を2重ループで走査する（無向グラフのため対角線および下三角は走査不要）。
    3. isConnected[i][j] == 1 の場合、都市 i と都市 j の間に辺が存在するため、union(i, j) を呼び出してグループを統合する。
    4. union 成功時にグループ総数をデクリメントし、すべての走査が完了した後の最終的なグループ総数 (group_count) を返す。
    """
    n = len(isConnected)
    uf = UnionFind(n)

    for i in range(n):
      for j in range(i + 1, n):
        if isConnected[i][j] == 1:
          uf.union(i, j)

    return uf.group_count
