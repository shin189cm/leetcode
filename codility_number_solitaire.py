# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""
問題：
配列Aで達成可能な最大の結果を返す return res
・A[0]は使う
・A[-1]も使う

制約条件：
Aの長さは、2以上10^5未満
Aの要素は、-10^4以上、10^4未満
6個以内を必ず使用した値にする

方針：
Aの先頭からi個までの値の最大値を、dp[i]として保存する。
ただし、サイコロの目ぶんしかジャンプできないため、6個以内のスコープで比較する。
手前6個までで、dp[i+j] = max(max(dp[i:i+6]), max(dp[i:i+6]) + A[i+j])をして、
そのcandidateの最大値をdp[i+j]にする
ただし、A[i+j]が負の場合は、max不要、、、
とはできない。なぜなら、要素を必ず使用する必要があるから。
要素を必ず使う、を実装する。

dp[i]を、A[i]を使う前提での最大値、とすればいいのか。
そうすれば、最後に、max(dp[n-6:n])で最大値を返せる

方針まとめ：
・A[i]を使う前提で、Aの先頭からi個までの値の最大値を、dp[i]として保存する。
・A[n-1]まで実行する
・最後にmax(dp[n-6:n])で最大値を返す

懸念点：
nが6以下の大きさだった場合、A[i]を使う前提を持たなくてもよいのでは

0,-1,3,-4,1
0,-1,2,-2,3
これ、本当は最後は4を返したい。

dpを更新するとき、

最後に使ったあと、使わなかった場合も値を持っておく？のがいいのか？


"""
def solution(A):
    # Implement your solution here
    n = len(A)
    dp = [-float('inf')] * n
    dp[0] = A[0]

    for i in range(1,n):
        dp[i] = A[i] + max(dp[max(0, i-6):i])
    return dp[n-1]
