a = int(input())
b = int(input())
c = int(input())
x = int(input())//50
# X円を作る方法は、X-500円を作る方法＋+1と、X-100円を作る方法数+1と、50円の+1の和
# 50の倍数なので、問題をスケール縮小させよう
# 500→10
# 100→2
# 50→1
# X = X//50

# そもそも枚数不足は早期リターン
if 10 * a + 2 * b + c < x:
  print(0)

# dpはidx円を作る方法数
dp = [0] * (x+1)
dp[0] = 1
# 同じコインを何度も使えないように、for文の順番を降順にする
for i in range(1, x+1):
  for j in range(a+1):
    # もし、max
    for k in range(b+1):
      for l in range(c+1):
        if 
