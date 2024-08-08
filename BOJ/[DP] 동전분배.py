for _ in range(3):
    n = int(input())
    arr = []
    total = 0
    for _ in range(n):
        a,b = map(int, input().split())
        total += a*b
        arr.append((a,b))

    if total%2==1:
        print(0)
        continue
    
    total //=2
    
    dp = [True] + [False]*total
    for i in range(n):
        coin, cnt = arr[i]
        
        for idx in range(total, coin-1, -1):
            if dp[idx-coin]:
                for j in range(cnt):
                    if idx+coin*j<=total:
                        dp[idx+coin*j]=True
                    else:
                        break
                    
    if dp[-1]:
        print(1)
    else:
        print(0)
