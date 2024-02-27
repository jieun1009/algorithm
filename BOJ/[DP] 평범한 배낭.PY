n, k = map(int, input().split())
ls = [[0,0]]
for i in range(n):
    w,v = map(int, input().split())
    ls.append((w,v))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w,v = ls[i]
    for j in range(1, k+1):
        if j>=w: # 넣을 수 있음
            dp[i][j] = max(dp[i-1][j], v+dp[i-1][j-w])
        else: # 못넣음
            dp[i][j] = dp[i-1][j]
print(dp[n][k])