n, k = map(int,input().split())
arr = [(0,0)]
dp = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    w, v = map(int,input().split())
    arr.append((w, v))
    
for i in range(1,n+1): # 물건 하나씩
    for j in range(1,k+1): # 1~k무게까지 표 작성
        w = arr[i][0] # 무게
        v = arr[i][1] # 가치
        if j < w : # 현재 물건이 더 큰 경우, 이전 표값으로 넣기
            dp[i][j] = dp[i-1][j]
        else: # 해당 물건이 들어가는 사이즈인 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
            
print(dp[n][k])