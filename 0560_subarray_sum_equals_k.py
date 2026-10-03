"""
Problem: 560_subarray_sum_equals_k.py
URL: https://leetcode.com/problems/subarray-sum-equals-k/
Difficulty: Medium
Category: Array, Hash Table, Prefix Sum

Complexity:
- Time: O(N)
    - 配列 nums を先頭から末尾まで1回走査する (N は配列の長さ)
    - 各ループ内でのハッシュマップ（辞書）への検索・挿入・更新は平均 O(1)
    - 全体として O(N) で完了する
- Space: O(N)
    - 累積和の出現頻度を記録するハッシュマップ prefix_sum_count のサイズ
    - 最悪の場合、すべてのステップで異なる累積和が得られるため、格納される要素数は最大 N + 1 個となり O(N)

Approach:
1. 累積和 (Prefix Sum) と差分の関係を利用する
    - インデックス i までの累積和を prefix_sum[i] とする
    - 任意の区間 [j, i] (j <= i) の部分配列の和は prefix_sum[i] - prefix_sum[j - 1] で表せる
    - 部分配列の和が k となる条件は「prefix_sum[i] - prefix_sum[j - 1] = k」
    - 式を変形すると「prefix_sum[j - 1] = prefix_sum[i] - k」
2. ハッシュマップを用いた過去の累積和の検索
    - 走査中の現在地点の累積和を current_sum としたとき、過去に「current_sum - k」という累積和が
      何回出現したかをハッシュマップから O(1) で取得し、その回数を答えに加算する
    - 走査と同時に現在の current_sum をハッシュマップに記録（カウント更新）していく
3. 基底条件（初期値）の設定
    - 部分配列が先頭（インデックス 0）から始まってその時点で合計がちょうど k になるケースを拾うため、
      走査開始前に {0: 1}（和が 0 となる状態が 1 回存在）を登録しておく

memo:
- 「先頭からの2つの和（累積和）の差」が k と一致する組み合わせを探す問題。
- 現在の累積和から k を超えた分（current_sum - k）について、
  「先頭からの和がちょうどその余分な値と一致する区間」を過去から切り落とす（引き換える）ことで、
  末尾に current を含む区間の合計を k にできる。
- 「配列内の連続する部分配列の和」というキーワードで、要素に負数が含まれる場合、
  Sliding Window（しゃくとり法）は単調性が失われるため使用できない。
- 本問は LeetCode 1番 (Two Sum) と本質的に全く同じ発想であり、
  「走査しながら、過去に目的の差分 (current_sum - k) が存在したかを連想配列で探す」定石パターン。
- この「累積和 + ハッシュマップ」の組み合わせは、区間和に関する問題（特に余りの和、偶奇、特定値の一致など）で頻出。
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        # prefix_sum_count: 過去に出現した累積和とその出現回数を保持する
        # 初期状態として、何も足していない状態（和が 0）を 1 回として登録
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1

        for num in nums:
            current_sum += num

            # 先頭からの2つの和の差が k と一致する組み合わせを探す
            # current_sum から k を引いた余分な値 (target) が過去の累積和にあれば、
            # その先頭区間を引き換える（切り落とす）ことで合計 k の連続部分配列が作れる
            target = current_sum - k
            if target in prefix_sum_count:
                count += prefix_sum_count[target]

            # 現在の累積和をハッシュマップに記録
            prefix_sum_count[current_sum] += 1

        return count
