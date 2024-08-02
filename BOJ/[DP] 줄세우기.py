n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
dp = [0 for _ in range(n)]
dp[0]=1
max_val = 0
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]: # 증가수열 찾기
            # 현재 i 위치의 값이 0~i-1(j의 값)보다 클때 증가수열임
            # j의 dp 값에 +1 더한 것 만큼 길이가 가능
            # j까지는 다 크니까 i를 더하면 +1 길이임
            # 따라서 j의 dp 최대값을 구한 후 그 값에 +1을 더하면 dp[i]
            max_val = max(max_val, dp[j]) 
    dp[i] = max_val +1
    max_val = 0
print(n-max(dp))
# 즉 ans = n - 가장 긴 증가하는 부분수열 길이