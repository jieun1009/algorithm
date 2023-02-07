n=int(input())

dp = [[0]*10 for i in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1 
    
mod = 1000000000

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j]= dp[i-1][1] # 뒷자리가 0 일땐 뒤에 1밖에 못옴
        elif j ==9:
            dp[i][j] = dp[i-1][8] # 뒷자리가 9 일땐 뒤에 8밖에 못옴
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
            
print(sum(dp[n])% mod)