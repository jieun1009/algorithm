n = int(input())
arr = list(map(int,input().split()))

result = []
max_value = -1e9
visited=[False]*n
def dfs():
    global max_value
    if len(result) == n :
        total = 0
        for i in range(n-1):
            total += (abs(result[i]-result[i+1]))
        max_value = max(max_value, total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i]=True
            result.append(arr[i])
            dfs()
            visited[i]=False
            result.pop()

        

dfs()
print(max_value)
