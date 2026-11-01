"""Problem: 46_permutations.py

URL: https://leetcode.com/problems/permutations/
Difficulty: Medium
Category: Array, Backtracking

Complexity:
- Time: O(N * N!)
    - 要素数 N の順列の総数は N! 通り存在する。
    - 決定木（探索木）の葉ノードに至るたびに、長さ N の配列をコピーして結果に追加するため O(N) のコストが発生する。
    - 探索木の総ノード数は O(N!) のオーダーであり、全体で O(N * N!) となる。
- Space: O(N)
    - 呼び出しスタックの最大深さは N。
    - 訪問フラグ（visited）および現在構築中の経路配列（current）に消費する補助空間は O(N)。
    - （※ 結果返却用の O(N * N!) を除く補助記憶領域として評価）

Approach:
1. 深さ優先探索（DFS）とバックトラッキング（Backtracking）の適用:
    - 可変個数のループを「再帰呼び出し」で実現する。
    - 現在構築中の順列リスト current の長さが N に達したら、1つの順列が完成したとして結果リストにコピーを追加する。
2. 状態管理と復元（Undo）:
    - 各要素が使用済みかどうかを bool 配列（visited）で O(1) 管理する。
    - 探索木の枝を下る前に要素を追加し visited を True にする。
    - 再帰から戻った直後に要素を削除（current.pop()）し、visited を False に戻すことで、別分岐の探索に影響を与えないようにする。

memo:
- Python では `itertools.permutations` を使えば1行で解けるが、コーディングテストではバックトラッキングの実装力を評価されるため、自前で DFS/再帰を組む必要がある。
- 別解として配列をインプレースに swap しながら再帰するアプローチ（visited 配列が不要で空間効率が良い）もあるが、訪問配列を用いる標準的なバックトラッキング解法の方が直感的で拡張性（重複要素を含む LeetCode 47 への応用など）が高い。
"""

from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res: List[List[int]] = []
        visited = [False] * n
        current: List[int] = []

        def backtrack() -> None:
            # ベースケース: 順列が完成したら結果に追加（浅いコピーを作成）
            if len(current) == n:
                res.append(current[:])
                return

            for i in range(n):
                if not visited[i]:
                    # 状態を進める
                    visited[i] = True
                    current.append(nums[i])

                    # 次の要素を選びに行く
                    backtrack()

                    # 状態を戻す（Backtrack）
                    current.pop()
                    visited[i] = False

        backtrack()
        return res
