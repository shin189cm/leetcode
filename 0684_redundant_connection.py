from typing import List


class UnionFind:

  def __init__(self, n: int):
    # 1-indexed に対応するためサイズを n + 1 で確保
    self.parent = list(range(n + 1))
    self.size = [1] * (n + 1)

  def find(self, x: int) -> int:
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])  # 経路圧縮
    return self.parent[x]

  def union(self, x: int, y: int) -> bool:
    root_x = self.find(x)
    root_y = self.find(y)

    # 既に同じ代表元（親）を持つ場合、この辺を追加すると閉路ができるため結合失敗(False)
    if root_x == root_y:
      return False

    # Union by Size
    if self.size[root_x] < self.size[root_y]:
      root_x, root_y = root_y, root_x

    self.parent[root_y] = root_x
    self.size[root_x] += self.size[root_y]
    return True


class Solution:

  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    """Problem: 0684_redundant_connection.py

    URL: https://leetcode.com/problems/redundant-connection/
    Difficulty: Medium
    Category: Graph, Disjoint Set (Union-Find), Cycle Detection

    Complexity:
    - Time: O(N * alpha(N)) - 各エッジについて Union-Find 操作（Find/Union）を実行するため。alpha はアッカーマンの逆関数であり実質定数時間、全体で実質 O(N)（N: エッジ数およびノード数）
    - Space: O(N) - 頂点数 N に対応する parent 配列および size 配列（サイズ N + 1）を保持するため

    Approach:
    1. ノードが 1 から n まで存在するため、サイズ n + 1 で Union-Find を初期化する。
    2. edges 配列を先頭から順に走査し、各エッジ [u, v] に対して union(u, v) を試行する。
    3. u と v の根（代表元）がすでに同一である場合、このエッジを追加すると木構造が破綻して閉路（サイクル）が形成される。
    4. union(u, v) が False を返した時点で、そのエッジ [u, v] が閉路を完成させた最後の余分な辺であるため、直ちに結果として返す。
    """
    n = len(edges)
    uf = UnionFind(n)

    for u, v in edges:
      # すでに同一グループに属していれば、この辺がサイクルを形成する余分な辺
      if not uf.union(u, v):
        return [u, v]

    return []
