"""Problem: 207_course_schedule.py

URL: https://leetcode.com/problems/course-schedule/
Difficulty: Medium
Category: Graph, Topological Sort, Breadth-First Search (BFS)

Complexity:
- Time: O(V + E)
    - V はコース数（numCourses）、E は前提条件の数（prerequisites の長さ）
    - グラフ（隣接リスト）および入次数配列の構築に O(E)
    - 各ノードはキューに高々1回追加・取り出しされるため O(V)
    - 各エッジは探索中に高々1回走査されるため O(E)
    - 全体として線形時間 O(V + E) で完了する
- Space: O(V + E)
    - 隣接リスト形式のグラフ表現に O(V + E)
    - 入次数管理用の配列に O(V)
    - BFS用のキューに最大 O(V)

Approach:
1. 問題を有向グラフにおける「閉路検出（Cycle Detection）」と捉える
    - コースを頂点、前提条件 [a, b]（b を受講後に a が受講可能）を有向エッジ b -> a とする
    - 全てのコースが履修可能である条件は、グラフが有向非巡回グラフ（DAG）であること
2. Kahn's Algorithm（入次数を用いた BFS によるトポロジカルソート）
    - 各コースの入次数（＝履修に必要な未消化の前提条件の残数）を集計する
    - 初期状態で入次数が 0 のコース（前提条件なしですぐ履修できるもの）をキューに入れる
    - キューからコースを1つ取り出して履修完了とし、そのコースを前提としていた
      後続コース群の入次数を 1 減らす（前提条件を1つ消化）
    - 【重要】複数の前提を要するコース（例: AとBの履修が必須なC）は、1つ消化しただけでは
      受講できない。入次数をデクリメントした結果「残りの前提がすべて 0 になった瞬間」に
      初めて受講可能と判定し、キューに追加する
3. 判定
    - キューが尽きた時点で、履修完了したコース数が numCourses と一致すれば True
    - 一致しなければ、閉路（相互依存や堂々巡り）によって前提条件が 0 にならず
      キューに入れなかったコースが存在するため False

memo:
- 制約が V <= 2000, E <= 5000 であるため、O(V^2) の隣接行列アプローチや推移閉包の更新では
  メモリ・時間ともに非効率となりやすい。疎グラフであることを活かして隣接リスト + O(V + E) を採用する
- 閉路検出は DFS（3色塗り分け: White/Gray/Black）でも O(V + E) で実装可能だが、
  BFS（Kahn's Algorithm）は再帰のスタックオーバーフローのリスクがなく、直感的でバグが混入しにくい
- 11/18 模擬ライブコーディングでの学び（事前に方針を口頭で説明し、Claude に採点してもらった）:
    - [a, b] は for dest, src in prerequisites: のように分けて受け取る。
      item[0] / item[1] のままだと、graph と in_degree のどちらに何を入れるかで混乱しやすい。
      graph[src].append(dest)（src を履修すると前提が1つ減る先）、in_degree[dest] += 1。
    - graph[src] の値は「授業のリスト」。1つの授業が、複数の授業の前提になることがあるため。
    - 減算の複合代入は -=。=- と書くと x = -1 と解釈され、エラーにならずに気づきにくい。
    - for _ in range(len(queue)) で層を区切る書き方は不要。
      102（Level Order Traversal）のように「何層目か」を使う問題でだけ必要で、本問では層の情報を使わない。
    - 引数 numCourses を直接減らさず、completed_courses を別に数える。
      return True if x else False ではなく、比較式をそのまま返す。
    - 時間計算量の説明は、処理ごとに積み上げる（合計 3V + 2E → O(V + E)）:
      リストを作る V、prerequisites から埋める E、入次数0を探す V、
      キューからの取り出しは合計 V（入次数が0になる瞬間は1回しかないので、各授業がキューに入るのは最大1回）、
      内側のループは合計 E（全授業の graph の長さを合計すると、ちょうど E）。
      while の中に for があっても、掛け算にはならない。
    - 空間計算量は「リストの数 V ＋ 中身の合計 E」。graph を「各リストが最大 V 個だから V×V」と見積もると、
      実際より大きい上限になる。空のリストもそれ自体がメモリを使う（E = 0 でも V に比例）。
    - 循環があると False になる理由: 循環の中の授業は入次数が1以上。入次数は、前提となる授業が
      キューから取り出されたときにしか減らないが、その前提となる授業も同じ循環の中にあるため、
      キューに入らない。よって循環の中の授業はずっとキューに入らず、completed_courses が numCourses に届かない。
"""

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 3つ定義する。graph, in_degree, queue
        
        # そのコースを履修することが必要なコースリスト
        graph: list[list[int]] = [[] for _ in range(numCourses)]
        # そのコースを履修するために必要な他のコース数
        in_degree: list[int] = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # 事前に履修が不要なコース。最初に履修する。履修できるコースリスト
        queue: deque[int] = deque(
            course for course in range(numCourses) if in_degree[course] == 0
        )
        # 履修できたコース数
        completed_courses = 0

        # 履修できるコースがあるうちは
        while queue:
            # 1コース履修
            curr = queue.popleft()
            completed_courses += 1

            # 1コース履修したことで、履修できるようになるかもしれないコースたち
            for next_course in graph[curr]:
                in_degree[next_course] -= 1
                # もし履修できるようになったら履修できるコースリスト(queue)に追加
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return completed_courses == numCourses
