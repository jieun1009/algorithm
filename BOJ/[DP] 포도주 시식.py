n = int(input())
wine =[]
for _ in range(n):
    wine.append(int(input()))
dp = [0]*n
dp[0] = wine[0]
dp[1] = wine[0]+wine[1]
dp[2] = max(wine[2]+wine[0],wine[2]+wine[1],dp[1])


for i in range(3,n):
    dp[i] = max(wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3],dp[i-1])
    

print(max(dp))