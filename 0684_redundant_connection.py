"""Problem: 0684_redundant_connection.py

URL: https://leetcode.com/problems/redundant-connection/
Difficulty: Medium
Category: Graph, Disjoint Set (Union-Find), Cycle Detection

Complexity:
- Time: O(N * alpha(N)) 
  path halving と union by size を併用するため、
  各操作は償却で  O(alpha(N))（alpha はアッカーマン関数の逆関数で実質定数）。
  全体で実質 O(N)
  （N: エッジ数 = ノード数）
- Space: O(N) 
  parent 配列および size 配列（各サイズ N + 1）を保持するため

Approach:
1. 木（N ノード・N - 1 エッジ）に1本エッジを足すと、閉路がちょうど1つできる。
   「エッジ (u, v) を足すと閉路ができる」⇔「足す前から u と v がすでに連結している」。
2. ノードが 1 から n まで存在するため、parent をサイズ n + 1 で初期化する（1-indexed）。
3. edges を先頭から順に走査し、各エッジ [u, v] について find(u), find(v) で根を求める。
4. 根が一致する場合、u と v は別経路ですでに連結しているので、このエッジが閉路を完成させる余分な辺。
   直ちに [u, v] を返す。
5. 根が異なる場合は、片方の根をもう片方の根につなげて2つのグループを統合する。
6. 閉路を最初に完成させたエッジは、その閉路上のエッジのうち入力順で最後のものなので、
   「答えが複数あれば入力で最後のものを返す」という条件も自動的に満たす。

Note:
- 使う操作が find と単純な統合だけなので、UnionFind クラスを作らずに関数内で完結させている。
- find は再帰ではなく while ループで書き、parent[x] = parent[parent[x]]（path halving）で
  経路を短縮する。再帰の深さ制限を気にしなくてよい。
"""
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # 経路圧縮（path halving）
                x = parent[x]
            return x

        for u, v in edges:
            root_u, root_v = find(u), find(v)
            # すでに同じ根を持つ = 連結済み → この辺が閉路を形成する余分な辺
            if root_u == root_v:
                return [u, v]
            # union by size：小さいグループを大きいグループの下につなぐ
            if size[root_u] > size[root_v]:
                root_u, root_v = root_v, root_u
            parent[root_u] = root_v
            size[root_v] += size[root_u]

        return []

        # -----------------------------------------
        # 時間計算量が N log(N) になる、シンプルケース
        # -----------------------------------------
        """
        n = len(edges)
        parent = list(range(n + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # 経路圧縮（path halving）
                x = parent[x]
            return x

        for u, v in edges:
            root_u, root_v = find(u), find(v)
            # すでに同じ根を持つ = 連結済み → この辺が閉路を形成する余分な辺
            if root_u == root_v:
                return [u, v]
            parent[root_u] = root_v

        return []
        """
