result = []
def dfs(start, result):
    if len(result) == 6:
        print(*result)
        return
    
    for i in range(start,k+1):
    
        if len(result)==0:
            result.append(arr[i])
            dfs(i+1, result)
            result.pop()
        else: 
            # arr엔 숫자가 순서대로 들어있으니 result[-1]보다 크면
            # result에 더 들어갈 수 있는 상태!
            if arr[i] > result[-1]:
                result.append(arr[i])
                dfs(i+1, result)
                result.pop()
        

while(True):
    arr = list(map(int, input().split()))
    k = arr[0]
    if k ==0:
        break
    dfs(1,result)
    print()