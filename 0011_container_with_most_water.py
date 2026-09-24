"""Problem: 0011_container_with_most_water.py

URL: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Category: Two Pointers, Greedy

Complexity:
- Time: O(N)
    - 左右のポインタ（left, right）が配列の両端からスタートし、各ループで必ずどちらか一方が1ステップ内側に進む。
    - ポインタが交差する（left == right）までに走査する要素数は高々 N 回であるため、全体計算量は O(N)。
- Space: O(1)
    - ポインタ（left, right）および最大面積を保持する変数のみを管理するため、定数メモリ空間で動作する。

Approach:
1. 容器の水量は「底辺の長さ（幅）」と「2本の線のうち低い方の高さ」の積で決まる:
    area = min(height[left], height[right]) * (right - left)
2. Two Pointers（貪欲法）による探索空間の縮小:
    - left = 0, right = len(height) - 1 の最大幅から探索を開始する。
    - 面積のボトルネックは常に「低い方の壁」である。
    - 仮に「高い方の壁」を内側に動かしても、幅 (right - left) が狭まる上に、高さの上限は低い方の壁に抑えられたまま（あるいはさらに低くなる）であるため、現在の面積を上回ることは絶対にあり得ない。
    - したがって、現在の状態より面積が大きくなる可能性がある唯一の選択肢は「低い方の壁を内側に進めること」のみである。
3. 終了条件:
    - 左右のポインタが衝突した時点で全探索空間の最適解が検証されたことが保証されるため、ループを抜けて最大値を返す。

memo:
- 「全探索 O(N^2) では制約 N <= 10^5 に耐えられない」と即座に判断し、O(N) または O(N log N) のアプローチを想起することが最重要。
- DP（動的計画法）を検討しがちだが、部分問題の最適構造というよりは「探索候補の安全な間引き（Greedy Elimination）」が成立するため、Two Pointers が最適解となる。
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h_left = height[left]
            h_right = height[right]

            # 現在の幅と律速している高さから面積を算出
            current_width = right - left
            current_height = min(h_left, h_right)
            current_area = current_width * current_height

            if current_area > max_area:
                max_area = current_area

            # 低い方のポインタを内側へ進める（同値の場合はどちらを進めてもよい）
            if h_left < h_right:
                left += 1
            else:
                right -= 1

        return max_area
