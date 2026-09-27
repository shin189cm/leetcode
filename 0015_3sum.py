"""
Problem: 15_3sum.py
URL: https://leetcode.com/problems/3sum/
Difficulty: Medium
Category: Array, Two Pointers, Sorting

Complexity:
- Time: O(N^2)
    - 配列のソートに O(N log N)
    - 外側ループで 1 要素を固定（高々 N 回）
    - 内側で左右のポインタを用いた挟み撃ち探索が各ステップで高々 N 回実行される
    - 全体計算量は O(N log N + N^2) = O(N^2) となり、N <= 3000 に対して約 9 * 10^6 回の操作で十分 TLE を回避可能
- Space: O(1) または O(N)
    - 外部の追加データ構造（ハッシュセットなど）は使用せず、ポインタ操作のみで完結するため補助空間は O(1)
    - Python の Timsort の内部実装に伴う一時的なメモリ使用量は O(N)
    - （出力用のリスト res は計算量定義から除外）

Approach:
1. 配列の事前ソート
    - 配列 nums を昇順ソートする。これにより、ポインタの移動方向と合計値の増減が単調増加/減少の関係になり、Two Pointers による挟み撃ちが可能になる
    - また、重複する値を隣接させることで、同一値のスキップ処理が容易になる
2. 1要素固定 + Two Pointers による 2Sum 探索
    - インデックス i を 0 から len(nums) - 1 まで走査し、第1要素 nums[i] を固定する
    - 探索対象の目標値 target を -nums[i] とする
    - left = i + 1, right = len(nums) - 1 としてポインタを配置
    - nums[left] + nums[right] が target より小さければ left を右へ進めて和を増やし、大きければ right を左へ進めて和を減らす
    - 一致した場合は組み合わせを res に追加
3. 重複要素の枝刈りとスキップ
    - 外側ループ: i > 0 かつ nums[i] == nums[i-1] の場合は探索済みの値であるため continue
    - 早期終了: ソート済みのため、nums[i] > 0 となった時点で以降の3要素の和が 0 になることはあり得ないため break
    - 内側ポインタ: 解を発見した後、left と right それぞれについて隣接する同値要素をスキップするまでポインタを進める

memo:
- 「3要素の和」は愚直に探索すると O(N^3) だが、「ソート + 1要素固定の 2Sum」に帰着させることで O(N^2) に落とすのが定石パターン
- ハッシュテーブル（Set）を用いて解くアプローチ（各要素について 2Sum を解く）も存在するが、
  重複する三つ組の除去処理で余分な空間計算量 O(N) やハッシュオーバーヘッドがかかるため、
  実務・コーディングテストともに「ソート + Two Pointers」が最も空間効率が良く推奨される
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # 最小の値が正であれば、どう組み合わせても合計0にはならないため終了
            if nums[i] > 0:
                break

            # 1つ目の要素の重複をスキップ
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # 2つ目・3つ目の要素の重複をスキップ
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res
