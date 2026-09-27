"""Problem: 238_product_of_array_except_self.py

URL: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Category: Array, Prefix Sum

Complexity:
- Time: O(n)
    - 配列 nums の長さを n とする。
    - 左から右への走査で n 回の乗算と代入を行う。
    - 右から左への走査で n 回の乗算と更新を行う。
    - 合計の操作回数は 2n 回となり、全体計算量は O(n)。
- Space: O(1) Extra Space
    - 問題文の定義に従い、返却用の出力配列 ans は追加空間としてカウントしない。
    - アルゴリズム内で追加利用するメモリは、右側からの累積積を保持するスカラー変数 suffix のみであり O(1)。
    - (出力配列を含めた全体空間計算量としては O(n))

Approach:
1. 構造の分解:
    - 任意の要素 i について、「自分以外の全要素の積」は
      (インデックス 0 から i-1 までの積) * (インデックス i+1 から n-1 までの積)
      すなわち「左側の累積積 (prefix)」と「右側の累積積 (suffix)」の積に分解できる。
2. 左側累積積の記録 (Pass 1):
    - 長さ n の配列 ans を作成し、ans[0] = 1 とする。
    - i = 1 から n-1 まで走査し、ans[i] = ans[i-1] * nums[i-1] を計算して格納する。
    - これにより、ans[i] には nums[i] より左側の全要素の積が入る。
3. 右側累積積の合成 (Pass 2):
    - 変数 suffix = 1 を用意する。
    - i = n-1 から 0 まで逆順に走査する。
    - 現在の ans[i] (左側の積) に suffix (右側の積) を掛け合わせて ans[i] を更新する。
    - 次の要素のために suffix に nums[i] を掛け合わせる (suffix *= nums[i])。
4. 完了:
    - 全要素を合成した ans を返却する。

memo:
- 「全要素の積 / nums[i]」という除算解法は、除算禁止制約だけでなく「要素に 0 が含まれるケース」でゼロ除算例外（ZeroDivisionError）を引き起こすため本質的に不適。
- 累積和（Prefix Sum）の掛け算版（Prefix Product）として捉えるのが定石。
- 左右それぞれに O(n) の補助配列（prefix 配列、suffix 配列）を用意する解法でも正解にはなるが、コーディングテストでは出力配列を再利用して O(1) 空間に最適化する手法まで実装できて初めて満点評価となる点に注意。
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n

        # Pass 1: 左側からの累積積を ans に格納
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        # Pass 2: 右側からの累積積を変数で保持しながら掛け合わせる
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
