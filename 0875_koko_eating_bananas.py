"""
Problem: 875_koko_eating_bananas.py
URL: https://leetcode.com/problems/koko-eating-bananas/
Difficulty: Medium
Category: Binary Search (Binary Search on Answer)

Complexity:
- Time: O(N * log(M))
    - N は piles の長さ (len(piles))、M はバナナの山の最大値 (max(piles))
    - 探索範囲は [1, M] であり、二分探索のイテレーション回数は O(log M) 回
    - 各イテレーションにおいて、全 N 個の山に対して必要時間を計算するため O(N)
    - 全体計算量は O(N * log M)
- Space: O(1)
    - 探索用のポインタ変数（left, right, mid）および累積時間を保持する変数のみを使用するため、追加メモリは定数倍

Approach:
1. 問題の単調性に着目（最適化問題から判定問題への帰納）
    - 食べる速度 k が速くなるほど、全バナナを食べきるのに必要な総時間は単調減少（または同一）する
    - 「速度 k で h 時間以内に食べきれるか？」というブール値の判定関数 f(k) は、ある境界値を境に False から True に切り替わる
    - この単調性を利用し、k の最小値を求めるために答えの値域に対する二分探索を行う
2. 探索境界の設定
    - left = 1: 最低でも毎時 1 本は食べる必要がある
    - right = max(piles): h >= len(piles) の制約下では、最大値以上の速度を出しても各山で 1 時間消費するため、max(piles) が上限となる
3. 判定ロジックと境界の更新
    - 中間値 mid = (left + right) // 2 について、総所要時間 hours を計算
    - 各山 p に対する消費時間は ceil(p / mid) であり、整数除算を用いて (p + mid - 1) // mid で算出可能
    - hours <= h（間に合う）場合:
        - mid が答えの候補となるため、right = mid として左側（より小さい速度）を探索
    - hours > h（間に合わない）場合:
        - mid では不足しているため、left = mid + 1 として右側を探索
4. 終了条件
    - left == right となった時点で探索終了し、その値が最小の k となる

memo:
- 「〜を満たす最小/最大値を求めよ」かつ「値が大きくなれば（小さくなれば）条件を満たしやすくなる」という構造を持つ問題は、
  真っ先に「答えで二分探索（Binary Search on Answer）」を検討する
- 各要素の除算の切り上げは math.ceil(p / mid) でも可能だが、浮動小数点数の精度問題を回避するため
  整数除算 (p + mid - 1) // mid を用いるのが定石
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                right = mid
            else:
                left = mid + 1

        return left
