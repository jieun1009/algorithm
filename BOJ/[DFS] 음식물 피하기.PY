import sys
sys.setrecursionlimit(10**6)

n,m,k = map(int, input().split())
graph = [[0]*(m+1) for i in range(n+1)]

for i in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def dfs(x, y):
    global cnt

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx<0 or nx> n or ny<0 or ny> m:
            continue
        if graph[nx][ny]==1:
            graph[nx][ny]=0
            cnt+=1
            dfs(nx, ny)


result = -1
for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j]==1:
            cnt=1
            graph[i][j]=0
            dfs(i, j)
            result = max(result, cnt)

print(result)