"""Problem: 0035_search_insert_position.py

URL: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy
Category: Binary Search

Complexity:
- Time: O(log N) - 各ステップで探索範囲を半分に縮小するため（N: 配列の要素数）
- Space: O(1) - 定数個のポインタ変数のみを使用するため

Approach:
1. 探索範囲を半開区間 [left, right) として設定する（left = 0, right = len(nums)）。
   right を len(nums) にすることで、target が全要素より大きい場合の挿入位置（末尾）も扱える。
2. left < right の間、中央値 mid を算出して二分探索を実行する。
3. nums[mid] < target なら、mid 以下の位置に答えはないため left = mid + 1 とする。
4. nums[mid] >= target なら、mid が答えの候補なので残したまま right = mid とする。
5. left == right でループを抜けたとき、left は「target 以上の最初の位置」を指している。
   target が存在すればその位置、存在しなければ挿入位置になるため、left を返却する。
   不変条件: nums[:left] < target, nums[right:] >= target

Notes: lower_bound / upper_bound（半開区間 [left, right) 版）
- 初期値は left = 0, right = len(nums)。while left < right の間ループする。
- 違いは nums[mid] == target のとき、どちらの端を動かすかだけ。

- `<` 版（lower_bound）:
    if nums[mid] < target: left = mid + 1
    else:                  right = mid
  nums[mid] == target のときは right = mid で右端を縮める。
  left は target 未満の要素しか越えないので、left == right でループを抜けたとき、
  left は target 以上の最初の位置になっている。
  不変条件: nums[:left] < target, nums[right:] >= target

- `<=` 版（upper_bound）:
    if nums[mid] <= target: left = mid + 1
    else:                   right = mid
  nums[mid] == target のときは left = mid + 1 で左端を進める。
  left は target 以下の要素を全部越えるので、left == right でループを抜けたとき、
  left は target より大きい最初の位置になっている。
  不変条件: nums[:left] <= target, nums[right:] > target

- 応用:
  - target の個数 = upper_bound - lower_bound
  - target が最後に出てくる位置 = upper_bound - 1（target が存在する場合）
  - Python 標準ライブラリでは bisect.bisect_left / bisect.bisect_right に対応する。
  - 例: nums = [1, 2, 2, 2, 3], target = 2 → lower_bound = 1, upper_bound = 4, 個数 = 3
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
