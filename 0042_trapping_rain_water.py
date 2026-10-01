"""
Problem: 42_trapping_rain_water.py

URL: https://leetcode.com/problems/trapping-rain-water/
Difficulty: Hard
Category: Two Pointers, Dynamic Programming, Monotonic Stack

Complexity:
- Time: O(N)
    - N は配列 height の長さ
    - 左右のポインタ left, right が両端から中央に向かって進み、各要素を高々1回しか訪問しないため O(N)
- Space: O(1)
    - 左右の最大値およびポインタ管理に必要な定数個の変数のみを使用するため O(1)
    - (※ DP テーブルを用いたアプローチでは O(N) となる)

Approach:
1. 問題の本質（各マスの水深の定式化）
    - インデックス i に溜まる水の量は、以下の式で完全に決定される:
      water[i] = max(0, min(left_max[i], right_max[i]) - height[i])
      ここで left_max[i] は 0..i の最大値、right_max[i] は i..N-1 の最大値
2. Two Pointers による空間 O(1) への最適化
    - 配列の両端にポインタ (left = 0, right = N - 1) を配置し、それぞれの側から見た最大値 (left_max, right_max) を追跡する
    - left_max < right_max の場合:
      left から見た「右側の真の最大値」が未確定であっても、少なくとも right_max 以上の壁が存在することは確定している。
      したがって、left 地点における水面高さは確実に left_max によって律速される (min(left_max, right_max) = left_max)。
      よって、total_water += left_max - height[left] を加算し、left += 1 と進める
    - left_max >= right_max の場合:
      同様の対称性により、right 地点における水面高さは確実に right_max によって律速される。
      total_water += right_max - height[right] を加算し、right -= 1 と進める
3. 境界条件の処理
    - 要素数が 2 以下の場合は水が溜まる余地がないため、即座に 0 を返す

memo:
- 「区間を切り出して水槽を作る」という発想だと、複雑な形状（W型など）に対応する分岐が指数関数的に増えて破綻する
- 「各インデックス単体に溜まる水の量」に分解し、それを決定する支配要因（ボトルネック）を特定することがブレークスルーになる
- 別解として「単調減少スタック (Monotonic Stack)」を用いる手法もある。
  こちらは横方向（層状）に水を回収していくアプローチであり、スタック操作の理解として有益だが、
  面接やコーディングテストでは実装が簡潔かつ空間 O(1) の Two Pointers が第一選択となる
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        if not height or len(height) <= 2:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water
