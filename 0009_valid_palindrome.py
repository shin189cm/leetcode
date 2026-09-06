# 0009 Valid Palindrome (※LeetCode 9 は Palindrome Number)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        left, right = x, 0

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        while left > right:
            right = right * 10 + left % 10
            left = left // 10

        return left == right or left == right // 10

# Time: O(N) 桁数/2
# Space: O(1) 保存用のみ

"""
フィードバック
 タイトルの混同: LeetCode 0009 の問題名は Palindrome Number です（「Valid Palindrome」は文字列を扱う LeetCode 125）。
 計算量の表記揺れ:
 入力値 x に対して、桁数は \log_{10}(x) です。
 「桁数を N とする」と定義するなら O(N) で問題ありませんが、アルゴリズムの文脈で単に O(N) と書くと「数値の大きさ x に対して線形」と誤解されやすいため、O(\log_{10} x) または「N 桁として O(N)」と明記するのが安全です。
 ガード節の位置:
 ⁠left, right = x, 0⁠ の初期化を ⁠if x < 0 or ...⁠ の後に行うと、即時リターン時に無駄な変数バインドが発生しません。
 アルゴリズム自体は最適:
 文字列変換を避けて数値を半分だけ反転させるアプローチ（オーバーフロー回避・空間 O(1)・偶数奇数桁の両対応）は LeetCode 9 の模範解答通り正確に実装されています。

"""