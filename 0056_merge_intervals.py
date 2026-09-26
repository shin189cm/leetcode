"""
Problem: 56_merge_intervals.py
URL: https://leetcode.com/problems/merge-intervals/
Difficulty: Medium
Category: Array, Sorting

Complexity:
- Time: O(N log N)
    - 入力区間リストの長さを N とする
    - 区間の開始点 (start) に基づくソートに O(N log N) を要する
    - ソート後の線形走査は各区間を1度ずつ確認するのみなので O(N)
    - 全体の計算量はソートがボトルネックとなり O(N log N)
- Space: O(N)
    - Python の Timsort (list.sort) は最悪ケースで O(N) の作業領域を消費する
    - マージ結果を格納するリスト merged に最大で入力と同じ O(N) のメモリを要する

Approach:
1. 区間の開始値によるソート
    - 各区間 intervals[i] = [start_i, end_i] を start_i の昇順でソートする
    - これにより、走査時点で「新しく登場する区間の start は、すでに処理した区間の start 以上である」という不変条件が成立する
2. 逐次線形走査とマージ判定
    - 結果リスト merged が空、または「直前の区間の end」<「現在の区間の start」の場合:
        - 重複は発生しないため、現在の区間をそのまま merged に追加する
    - それ以外（「直前の区間の end」>=「現在の区間の start」）の場合:
        - 区間が重複しているため、直前の区間の終了点を拡張する
        - merged[-1][1] = max(merged[-1][1], current_end)
3. 走査終了後、merged を返却

memo:
- 区間スケジューリングや区間結合の問題における第一選択は「端点（start または end）でのソート」である
- 本問では start でソートすることで、「過去の複数の区間と同時に重複する可能性」を排除し、直前に追加した区間との比較のみに計算を落とし込める
- 空間計算量を O(1)（出力用配列を除く）に抑える要件がある場合は、ソート済みの配列に対して 2-pointer (In-place) で書き換える手法も存在する
"""


class Solution:

  def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
      return []

    # start の昇順でソート (O(N log N))
    intervals.sort(key=lambda x: x[0])

    merged: list[list[int]] = []

    for interval in intervals:
      # merged が空、または重複がない場合はそのまま追加
      if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
      else:
        # 重複している場合は、直前区間の end を大きい方で更新
        merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
