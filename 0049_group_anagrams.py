"""
Problem: 49_group_anagrams.py
URL: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Category: Array, Hash Table, String, Sorting

Complexity:
- Time: O(N * K * log K)
    - N は strs の要素数、K は文字列の最大長
    - 各文字列 s に対し、文字列のソート処理 sorted(s) に O(K log K)
    - 長さ K の文字列の結合 "".join(...) およびハッシュ化に O(K)
    - これを全 N 個の文字列に対して実行するため、全体で O(N * K log K)
    - （※各文字のカウントをタプル化する手法をとれば O(N * K) も可能だが、
      本問の制約 K <= 100 ではソート手法の方がオーバーヘッドが小さく高速）
- Space: O(N * K)
    - ハッシュマップ ans に格納される全キーの総文字数が最大 O(N * K)
    - ハッシュマップの各バリューに格納される全文字列の参照が O(N)
    - 返り値として構築される2次元リストに O(N * K)

Approach:
1. アナグラムの同値類のモデル化
    - 2つの文字列がアナグラムであることの必要十分条件は「ソート後の文字列が一致すること」
    - したがって、「ソート後の文字列」をハッシュマップのキー（正規化キー）として採用する
2. ハッシュマップ（collections.defaultdict）による一括集約
    - キーを tuple または str（ソート後）、バリューを同一グループに属する文字列のリストとする
    - strs を 1 度走査し、各文字列をキーに対応するリストに追加する
3. 走査終了後、ハッシュマップの value 一覧をリスト化して返却する

memo:
- 文字の出現頻度配列（要素数26のタプル）をキーにする O(N * K) 解法も存在するが、
  Python ではタプルのハッシュ生成コストがあるため、K <= 100 程度の短さであれば
  C言語実装された組込関数 sorted() による O(N * K log K) の方が実測で速いケースが多い
- 未知のグループを逐次比較するのではなく、「全単語を一意な標準形に写像してバケットに放り込む」
  という発想の転換がハッシュテーブル問題の定石
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())
