n = int(input())
arr= list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]

max_val = 0
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]: # 증가 수열임!
            
            max_val = max(max_val, dp[j])    
           
    dp[i] = max_val + arr[i]
    max_val= 0
print(max(dp)) 