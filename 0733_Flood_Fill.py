"""
Problem: 0733_flood_fill.py
URL: https://leetcode.com/problems/flood-fill/
Difficulty: Easy
Category: DFS, Grid, Graph

Complexity:
- Time: O(M * N) - 各セルを最大1回走査するため（M: 行数, N: 列数）
- Space: O(M * N) - 全セルが連結している最悪ケースにおける再帰のコールスタックの深さ（Recursion Depth）

Approach:
1. 開始地点の色 (orig_color) と変更後の目標色 (color) が同じ場合は、変更不要かつ無限ループ防止のため即座に返却する。
2. 開始地点から上下左右の4方向に対して深さ優先探索 (DFS) を再帰的に実行する。
3. 探索先がグリッド範囲外、または元の色 (orig_color) と異なる場合は探索を終了する。
4. 有効なセルの色を目標色に塗り替え、隣接する4方向へ同様の探索を伝播させる。
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(r: int, c: int) -> None:
            if not (0 <= r < m and 0 <= c < n) or image[r][c] != orig_color:
                return

            image[r][c] = color

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image
