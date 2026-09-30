"""Problem: 930_binary_subarrays_with_sum.py

URL: https://leetcode.com/problems/binary-subarrays-with-sum/
Difficulty: Medium
Category: Array, Hash Table, Prefix Sum, Sliding Window

Complexity:
- Time: O(N)
    - 配列 nums（長さ N）を1回走査する。
    - 各要素に対する累積和の計算、ハッシュマップ（defaultdict）の参照および更新は平均 O(1)。
    - 全体として O(N) の線形時間で完了する。
- Space: O(N)
    - 累積和の出現頻度を記録するハッシュマップ counts を保持する。
    - 累積和の取りうる値は 0 から N までの最大 N + 1 通りであるため、空間計算量は O(N)。

Approach:
1. 累積和（Prefix Sum）と差分の利用
    - 区間 [i, j] の総和は prefix_sum[j] - prefix_sum[i - 1] で表される。
    - したがって、prefix_sum[j] - prefix_sum[i - 1] = goal となる i の個数を求めればよい。
    - 式を変形すると prefix_sum[i - 1] = prefix_sum[j] - goal となる。
2. ハッシュマップによる過去状態の集計
    - 走査中の現在地点までの累積和を current_sum とする。
    - 過去の地点において累積和が (current_sum - goal) であった回数を counts から取得し、答えに加算する。
    - 初期状態として「和が 0 である地点が 1 回存在した」とみなすため counts[0] = 1 で初期化する。
3. Sliding Window との比較
    - 本問は「atMost(goal) - atMost(goal - 1)」という尺取り法を用いることで Space O(1) に最適化可能。
    - しかし、要素に 0 が含まれる配列における厳密一致カウントでは、ポインタ操作の境界条件や goal = 0 の
      エッジケースでバグが頻発しやすい。
    - 面接やテストの本番では、実装が明瞭でミスが生じにくい Prefix Sum + Hash Map をまず確実に実装すべき。

memo:
- 「和が K となる連続部分配列の数」を数える問題（LeetCode 560: Subarray Sum Equals K など）の典型パターン。
- 負の値が含まれる場合でも Prefix Sum 解法はそのまま成立するが、尺取り法は単調性が失われて破綻する。
  適用可能な条件（汎用性）の観点からも Prefix Sum の理解を固めておくことが極めて重要。
"""

from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        counts: dict[int, int] = defaultdict(int)
        counts[0] = 1
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            current_sum += num
            target = current_sum - goal
            if target in counts:
                total_subarrays += counts[target]
            counts[current_sum] += 1
            
        return total_subarrays
