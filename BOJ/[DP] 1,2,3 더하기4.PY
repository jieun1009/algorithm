t = int(input())


for _ in range(t):
    n = int(input())
    # 1만 쓰는 방법은 모두 1개씩 가지므로 1로 초기화
    dp=[1]*(n+1)
    # dp에 2가 추가된다면 dp[i-2]에서 2를 더하면 되므로 i-2 추가(3도 마찬가지)
    for i in range(2,n+1):
        dp[i]+=dp[i-2]
    for i in range(3,n+1):
        dp[i]+=dp[i-3]
        
    print(dp[n])