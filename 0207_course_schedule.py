"""Problem: 207_course_schedule.py

URL: https://leetcode.com/problems/course-schedule/
Difficulty: Medium
Category: Graph, Topological Sort, Breadth-First Search (BFS)

Complexity:
- Time: O(V + E)
    - V はコース数（numCourses）、E は前提条件の数（prerequisites の長さ）
    - グラフ（隣接リスト）および入次数配列の構築に O(E)
    - 各ノードはキューに高々1回追加・取り出しされるため O(V)
    - 各エッジは探索中に高々1回走査されるため O(E)
    - 全体として線形時間 O(V + E) で完了する
- Space: O(V + E)
    - 隣接リスト形式のグラフ表現に O(V + E)
    - 入次数管理用の配列に O(V)
    - BFS用のキューに最大 O(V)

Approach:
1. 問題を有向グラフにおける「閉路検出（Cycle Detection）」と捉える
    - コースを頂点、前提条件 [a, b]（b を受講後に a が受講可能）を有向エッジ b -> a とする
    - 全てのコースが履修可能である条件は、グラフが有向非巡回グラフ（DAG）であること
2. Kahn's Algorithm（入次数を用いた BFS によるトポロジカルソート）
    - 各コースの入次数（＝履修に必要な未消化の前提条件の残数）を集計する
    - 初期状態で入次数が 0 のコース（前提条件なしですぐ履修できるもの）をキューに入れる
    - キューからコースを1つ取り出して履修完了とし、そのコースを前提としていた
      後続コース群の入次数を 1 減らす（前提条件を1つ消化）
    - 【重要】複数の前提を要するコース（例: AとBの履修が必須なC）は、1つ消化しただけでは
      受講できない。入次数をデクリメントした結果「残りの前提がすべて 0 になった瞬間」に
      初めて受講可能と判定し、キューに追加する
3. 判定
    - キューが尽きた時点で、履修完了したコース数が numCourses と一致すれば True
    - 一致しなければ、閉路（相互依存や堂々巡り）によって前提条件が 0 にならず
      キューに入れなかったコースが存在するため False

memo:
- 制約が V <= 2000, E <= 5000 であるため、O(V^2) の隣接行列アプローチや推移閉包の更新では
  メモリ・時間ともに非効率となりやすい。疎グラフであることを活かして隣接リスト + O(V + E) を採用する
- 閉路検出は DFS（3色塗り分け: White/Gray/Black）でも O(V + E) で実装可能だが、
  BFS（Kahn's Algorithm）は再帰のスタックオーバーフローのリスクがなく、直感的でバグが混入しにくい
"""

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph: list[list[int]] = [[] for _ in range(numCourses)]
        in_degree: list[int] = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        queue: deque[int] = deque(
            course for course in range(numCourses) if in_degree[course] == 0
        )
        completed_courses = 0

        while queue:
            curr = queue.popleft()
            completed_courses += 1

            for next_course in graph[curr]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return completed_courses == numCourses
