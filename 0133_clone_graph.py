"""Problem: 133_clone_graph.py

URL: https://leetcode.com/problems/clone-graph/
Difficulty: Medium
Category: Graph, Depth-First Search (DFS), Hash Table

Complexity:
- Time: O(V + E)
    - グラフの頂点数を V、エッジ数を E とする
    - ハッシュマップにより各ノードの複製は高々 1 回行われるため、ノード処理は O(V)
    - すべてのノードの隣接リスト (neighbors) の走査回数はエッジ数に比例し、合計 2 * E 回参照されるため O(E)
    - ハッシュマップの検索・挿入は平均 O(1) なので、全体計算量は O(V + E)
- Space: O(V)
    - 元ノードから新ノードへのマッピングを保持するハッシュマップ visited に O(V)
    - DFS の再帰呼び出しに伴うコールスタックの消費が最悪 O(V)（グラフが一連の直線状の場合）
    - 全体として O(V) の追加メモリを使用する

Approach:
1. 問題を「参照関係を維持した無向グラフのディープコピー問題」と捉える
    - 各ノードの val だけでなく、neighbors に含まれるポインタもすべて新規作成したノードを指す必要がある
    - グラフには閉路（サイクル）が存在するため、無限再帰を防ぐ訪問管理が必須
2. ハッシュマップ (visited) によるクローン管理
    - キーを「元のノード」、値を「新規作成したクローンノード」とする辞書を保持する
    - 探索中にすでに visited に存在するノードへ到達した場合は、新規作成せず既存のクローンノードを返す
3. DFS（深さ優先探索）による再帰的構築
    - node が None の場合は None を返す（エッジケース処理）
    - 未訪問のノードに到達したら即座に Node(node.val) を生成して visited に登録する
    - その後、node.neighbors の各隣接ノードに対して再帰的に dfs を呼び出し、返されたクローンを新ノードの neighbors に追加する
    - 最終的に始点ノードのクローンを返す

memo:
- Python の標準ライブラリ copy.deepcopy(node) でもパス自体は可能だが、コーディングテストではデータ構造とアルゴリズムの理解を問われているため不可
- DFS（再帰）だけでなく、collections.deque を用いた BFS（反復）でも同一の計算量 O(V + E) / O(V) で実装可能
- グラフ探索において「閉路の存在」を意識し、探索と同時にコピー済みインスタンスの参照解決を行う設計パターンとして頻出の典型題
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # 元ノード -> 新ノード の対応関係を保持する辞書
        visited = {}

        def dfs(current: 'Node') -> 'Node':
            # すでに複製済みの場合はそのクローンを返して閉路ループを防ぐ
            if current in visited:
                return visited[current]

            # 新しいノードを作成し、隣接ノードを探索する前に辞書へ登録する
            clone = Node(current.val)
            visited[current] = clone

            # 隣接ノードを再帰的にクローンし、neighbors リストに追加する
            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

# BFSの場合
"""
from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: 'Node | None') -> Optional['Node']:
        if not node:
            return None

        # 元ノード -> 複製ノード のマッピング
        cloned = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    # 未訪問なら複製を作成して辞書登録し、キューに追加
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # 複製ノード同士をエッジで繋ぐ
                cloned[curr].neighbors.append(cloned[neighbor])

        return cloned[node]
"""
