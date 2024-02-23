t = int(input())

n = int(input())
arr = list(map(int, input().split()))

# 누적합 리스트
sum_arr = [0]
for i in range(k):
    sum_arr.append(sum_arr[-1]+arr[i])

# DP[i][j] : i에서 j까지 합하는데 최소 비용
# DP[i][k] + DP[k+1][j] + sum(arr[i]~arr[j])
    
DP = [[0]*(n+1) for _ in range(n+1)]
for i in range(2, n+1): # 부분 파일의 길이
    for j in range(1,n+2-i): # 시작점
        DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)])+ (sum_arr[j+i-1] - sum_arr[j-1])

print(DP[1][n])