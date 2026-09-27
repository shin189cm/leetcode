class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Problem: 198_house_robber.py
        URL: https://leetcode.com/problems/house-robber/
        Difficulty: Medium
        Category: Dynamic Programming

        Complexity:
        - Time: O(N)
            - 配列 nums の長さ N に対し、先頭から末尾まで1回の走査（ループ）で完了するため O(N)
        - Space: O(1)
            - 遷移に必要な直前2つの状態（rob1: i-2軒目までの最大値、rob2: i-1軒目までの最大値）のみを変数として保持するため、定数空間 O(1)

        Approach:
        1. 問題の本質と部分構造
            - 各家 i に対して選択肢は2つ存在する：
                a. 家 i を盗む場合: 隣接する家 i-1 は盗めないため、得られる価値は「家 i-2 までの最大値 + nums[i]」
                b. 家 i を盗まない場合: 家 i-1 までの最大値をそのまま引き継ぐ（「家 i-1 までの最大値」）
            - したがって、家 i までの最大利益を dp[i] とすると漸化式は以下の通りとなる：
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        2. 空間最適化 (DP配列から定数空間へ)
            - dp[i] の計算には dp[i - 1] と dp[i - 2] の2つの値しか参照しない
            - 配列全体を保持する代わりに、2つのポインタ/変数で状態をスライド更新することで空間計算量を O(1) に削減する
                - rob1: 2軒前までの最大値（初期値: 0）
                - rob2: 1軒前までの最大値（初期値: 0）
            - 各ループごとに current = max(rob2, rob1 + num) を求め、rob1, rob2 = rob2, current と更新していく

        memo:
        - DPの基本問題（一次元DP）であり、「直前の状態に依存する制約（隣接する要素を連続で選べない）」を状態遷移に落とし込む典型パターン
        - 配列サイズ N が 0 または 1 の境界値に対しても、本実装（初期値を 0 とし、nums のループを回す構造）であれば追加の条件分岐なしで安全に処理可能
        - 発展問題として、家が円環状に並ぶ「213. House Robber II」が存在するが、そちらは「0番目を含めて末尾を除く場合」と「1番目を含めて末尾を含む場合」の2回本アルゴリズムを呼び出すことで解くことができる
        """
        # rob1: i-2軒目までの最大値
        # rob2: i-1軒目までの最大値
        rob1 = 0
        rob2 = 0

        for num in nums:
            # 「この家を盗まない場合(rob2)」と「この家を盗む場合(rob1 + num)」の大きい方
            current = max(rob2, rob1 + num)
            rob1 = rob2 # 次のループから見て2軒前までの値
            rob2 = current # 次のループから見て1軒前までの値

        return rob2
