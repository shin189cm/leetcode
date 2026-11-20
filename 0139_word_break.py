"""
Problem: 139_word_break.py
URL: https://leetcode.com/problems/word-break/
Difficulty: Medium
Category: Dynamic Programming, Hash Table, String, BFS

Complexity:
- Time: O(N * min(N, K) * K + M * K)
    - N: len(s), M: len(wordDict), K: max(len(word) for word in wordDict)
    - wordDict をハッシュセットに変換する初期コスト: O(M * K)
    - DP の外側ループが N 回。内側ループで確認する部分文字列の長さは高々 K
    - Python における文字列スライス s[j:i] の生成およびハッシュ検索コスト: O(K)
    - したがって全体の時間計算量は O(N * K^2 + M * K)（最悪ケース K=N のとき O(N^3) だが、
      K を考慮した枝刈りを行うことで実効計算量は大幅に抑えられる）
- Space: O(N + M * K)
    - DP 配列のサイズ: O(N)
    - ハッシュセット word_set の保持コスト: 全単語の総文字数 O(M * K)

Approach:
1. 問題の構造化
    - 文字列 s の先頭から i 文字目までの部分文字列 s[0:i] が、辞書内の単語の組み合わせで
      構成可能かどうかを真偽値で管理する（1次元 DP）。
2. 状態定義と遷移
    - dp[i]: s[0:i] が辞書内の単語で分割可能なら True、不可能なら False（長さ N + 1 の配列）
    - 基底条件: dp[0] = True（空文字列は常に分割可能）
    - 遷移: dp[j] == True であるような j (< i) が存在し、かつ部分文字列 s[j:i] が
      wordDict に含まれる場合、dp[i] = True とする
    - 別の書き方：dp[i] が True の位置 i から、長さ 1〜K の s[i:i+j] が辞書にあれば
      dp[i+j] = True にする（前に配る形）。計算量は同じ
3. 最適化（枝刈り）
    - 内側の探索範囲を「単語の最大長 K」に限定することで、無駄なスライス生成と検索を削減
    - list に対する in 検索（O(M)）を防ぐため、wordDict は事前に set に変換（O(1) 検索）

memo:
- 2026-11-20 再トライ：ノーヒントAC（約28分）。前に配る形（dp[i] が True なら dp[i+j] を True）で解いた。
  range の範囲（i + j <= n）でテストを何度か間違えた。
- 計算量で、単語数 M を掛けてしまった（300 × 20 × 1000 = 600万）。
  set の検索は、ハッシュ値を計算して、その番号の棚を直接見に行くので、単語数には比例しない。
  - set を作るとき：単語ごとに全文字を読んでハッシュ値を計算し、「ハッシュ値 % 棚の数」の棚に置く → 全単語の文字数 O(M * K)
  - 探すとき：ハッシュ値の計算 O(K) → 棚を直接見る O(1) → 本当に同じ文字列か比べる O(K)
  - s[i:i+j] のスライスも、長さ j の新しい文字列を作るので O(K)
  - 正しくは O(N * K^2)。制約で数えると 300 × 20 × 20 = 約12万回
- set の「O(1) 検索」は、文字列の長さを定数とみなした言い方。文字列のキーでは O(K) と答える。
  違う単語でも同じ棚に来る（衝突する）ことがあり、衝突が集中した最悪の場合は O(M * K)。
  Python の set は棚が埋まると自動で増やすので、普段は平均で考えてよい。
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(w) for w in word_set)
        n = len(s)

        # dp[i] は s の先頭 i 文字 (s[0:i]) が分割可能かどうかを表す
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # i から最大でも max_len だけ戻った地点までを探索対象とする
            start_idx = max(0, i - max_len)
            # 逆走査することで、s[j:i]が短くなり、素早くbreakできるようになる
            for j in range(i - 1, start_idx - 1, -1):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
