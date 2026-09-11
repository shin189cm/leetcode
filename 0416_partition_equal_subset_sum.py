from typing import List

"""Problem: 0416_partition_equal_subset_sum.py

URL: https://leetcode.com/problems/partition-equal-subset-sum/
Difficulty: Medium
Category: Dynamic Programming (0-1 Knapsack, Subset Sum)

Complexity:
- Time: O(N * target)
    - 合計値を sum_val、target = sum_val // 2、要素数を N とする。
    - 奇数の場合、および最大要素が target を超える場合は O(N) で即座に判定終了。
    - DPループでは、外側で N 個の要素を走査し、内側で target から num までの
      高々 target 回の更新を行うため、最悪計算量は O(N * target) となる。
      （※ target は数値の大きさに依存する擬多項式時間）
- Space: O(target)
    - 0 から target までの合計値が達成可能かを記録する長さ (target + 1) の
      1次元 boolean 配列（dp テーブル）のみを保持するため。

Approach:
1. 問題の定式化
    - 全要素の総和 sum_val が奇数の場合、均等な2分割は不可能なため False を返す。
    - 目標値を target = sum_val // 2 とし、「要素の合計が target となる
      部分集合が存在するか」を判定する 0-1 ナップサック問題に帰着させる。
    - 配列内の最大要素が target を超えている場合、その要素単体で target を
      オーバーするため、即座に False を返す（枝刈り）。
2. DPテーブルの定義と初期化
    - dp[j]: 合計値 j を作ることが可能かどうかを表す真偽値（boolean）。
    - dp[0] = True（要素を1つも選ばない状態で和 0 は常に作れる）。
    - その他はすべて False で初期化。
3. 状態遷移と逆順走査（0-1 制約の担保）
    - 各 num in nums について、j を target から num まで「降順」に走査する。
    - 遷移式: dp[j] = dp[j] or dp[j - num]
    - 降順に走査する理由:
      昇順に走査すると、同ループ内で更新された直後の dp[j - num]（現在の num を
      すでに含んだ状態）を参照してしまい、同じ数値を2回以上使ってしまう
      （Coin Change 等の完全ナップサック問題の挙動になる）のを防ぐため。
4. 早期終了
    - 走査途中で dp[target] が True に到達した時点で、以降のループを打ち切り True を返す。

memo:
- 「322. Coin Change」との対比:
    - Coin Change: 各コインは何枚でも使える（完全ナップサック）
      -> 1次元配列を「昇順」に回し、同じコインの再利用を許容する。
    - Partition Equal Subset Sum: 各要素は1回しか使えない（0-1 ナップサック）
      -> 1次元配列を「降順」に回すことで、前の要素イテレーションの結果のみを参照させる。
- Python特有の高速化テクニック:
    - 整数値のビットシフトを用いたビット演算DP（bitmask）を用いると、
      `bits |= bits << num` により C言語レベルの並列ビット演算で劇的に高速化可能。
      コーディング面接ではまずこの 1次元 boolean DP を論理立てて説明・実装することが標準。
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # 合計が奇数の場合は 2 等分不可
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # 最大値が目標値を超えていれば、その時点で達成不可
        if max(nums) > target:
            return False
        
        # dp[j] は合計 j を作れるかどうか
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # target から num まで逆順に走査
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
            
            # 早期終了: 途中で target が達成できたら即終了
            if dp[target]:
                return True
                
        return dp[target]

# =============================================================================
# 【参考情報】Python の @cache（メモ化再帰）を用いたトップダウン実装
#
# ■ 本質的な構造の比較:
#   - トップダウン:
#       「選ぶ / 選ばない」の決定木を辿るため、状態キーとして (i, rem) の
#       2次元タプルを保持し続ける必要がある（状態数: O(N * target)）。
#   - ボトムアップ:
#       逆順走査により過去の状態を破壊せずに上書きできるため、i の次元を
#       完全に消去して 1次元配列（サイズ: target + 1）に圧縮できる。
#
# ■ トップダウンが低速になる理由:
#   1. キャッシュのキー生成・検索コスト:
#      (i, rem) のタプル生成およびハッシュテーブル（dict）走査が毎回走る。
#   2. 関数呼び出しのオーバーヘッド:
#      再帰の深さに応じたスタックフレームの生成・破棄コストが大きい。
#   3. メモリ局所性の低下:
#      配列の連続メモリアクセスに比べ、キャッシュヒット率が落ちる。
# =============================================================================

"""
from functools import cache
from typing import List

class SolutionTopDown:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # 奇数は等分不可
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # 最大値が target を超えていたら不可
        if max(nums) > target:
            return False

        # 探索の高速化: 大きい数から試した方が target 超過の枝刈りが早く効く
        nums.sort(reverse=True)

        @cache
        def dfs(i: int, rem: int) -> bool:
            # 基底条件（成功）: ちょうど target 分を引いて 0 に到達
            if rem == 0:
                return True

            # 基底条件（失敗）: 超過した、または全要素を見終わった
            if rem < 0 or i == len(nums):
                return False

            # 1. nums[i] を選ぶ (rem - nums[i])
            # 2. nums[i] を選ばない (rem そのまま)
            # どちらか一方で True が出れば短絡評価（or）で即終了
            return dfs(i + 1, rem - nums[i]) or dfs(i + 1, rem)

        return dfs(0, target)
"""
