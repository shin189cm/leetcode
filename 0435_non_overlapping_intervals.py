"""Problem: 435_non_overlapping_intervals.py

URL: https://leetcode.com/problems/non-overlapping-intervals/
Difficulty: Medium
Category: Greedy, Sorting, Interval Scheduling

Complexity:
- Time: O(N log N)
    - 区間の総数を N とする
    - 区間の終了時刻（end）に基づくソートに O(N log N) を要する
    - ソート後のリストを先頭から末尾まで 1 回走査する処理は O(N)
    - 全体の時間計算量はソートがボトルネックとなり O(N log N)
- Space: O(1) または O(N)
    - 追加で保持する状態は直前に確定した区間の終了時刻 last_end とカウンタのみで O(1)
    - Python の組み込みソート（Timsort）が内部で消費する作業領域として最大 O(N) を要する

Approach:
1. 問題の言い換え（Interval Scheduling Problem）
    - 「削除する区間数を最小化する」は「重なり合わない区間の数を最大化する」ことと等価
    - 最大数の非重複区間を選定し、全区間数 N からその数を引いた値が最小削除数となる
2. 貪欲法（Greedy Algorithm）の適用基準
    - 各区間を終了時刻 intervals[i][1] の昇順でソートする
    - 「最も早く終了する区間」を優先して残すことで、後続の区間が使える残り時間を最大化できる
3. 1重走査による確定と判定
    - 直前に残した区間の終了時刻 last_end を保持する（初期値は -inf）
    - 現在の区間 [start, end] を順に見て、start >= last_end であれば衝突しないため採用し、last_end を更新
    - start < last_end であれば衝突するため削除対象としてカウントする

memo:
- 貪欲法の本質: 「終了時刻（end）をできるだけ手前に抑え、後続のために空き時間を最大化する」こと
  - そのため終了時刻が同一の区間が複数あっても、後続への影響（last_end）は同じなのでソート順（タイブレーク）を気にする必要がない
- 区間問題において「開始時刻でソートするか、終了時刻でソートするか」は典型的な分岐点
- 重複排除・最大区間選択は「終了時刻ソート」、区間のマージ（Merge Intervals: LC 56）は「開始時刻ソート」が定石
- list.sort() はインプレース変更で None を返すため、再代入して NoneType 例外を起こさないよう注意
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # 終了時刻 (x[1]) の昇順でソート（インプレース操作）
        intervals.sort(key=lambda x: x[1])

        num_delete = 0
        last_end = float("-inf")

        for start, end in intervals:
            if start >= last_end:
                # 重複なし：この区間を採用し、終了時刻を更新
                last_end = end
            else:
                # 重複あり：終了時刻が遅い側を切り捨てる（＝この区間を削除）
                # last_end更新しない
                num_delete += 1

        return num_delete
