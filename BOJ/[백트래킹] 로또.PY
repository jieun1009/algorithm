
result = []
def dfs(start, result, k):
    if len(result)==6:
        print(*result)
        return
   
    for i in range(start,k):
        if len(result)==0: 
            result.append(s[i])
            dfs(i+1, result,k)
            result.pop()
        else:
            if s[i] > result[-1]: # 더 커야 들어갈 수 있음
                result.append(s[i])
                dfs(i+1, result,k)
                result.pop()
        


while (True):
    arr = list(map(int,input().split()))
    k = arr[0]
    if k==0:
        break
    s = arr[1:]
    dfs(0,result,k)
    print()