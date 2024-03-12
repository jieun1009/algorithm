from collections import deque
import copy
n,m,k = map(int, input().split())
graph = [[0]*(m+1) for i in range(n+1)]

for i in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1

def bfs(x,y, graph):
    temp_graph = copy.deepcopy(graph)
    cnt =1
    queue = deque()
    queue.append((x,y))

    bx = [-1,0,1,0]
    by = [0,-1,0,1]

    while queue:
        a,b = queue.popleft()
        temp_graph[a][b]=0
        for i in range(4):
            nx = bx[i]+a
            ny = by[i]+b

            if nx<0 or nx>n or ny<0 or ny>m:
                continue
            if temp_graph[nx][ny]==1:
                cnt += 1
                queue.append((nx,ny))
                temp_graph[nx][ny]=0

    return cnt

result = []
for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j]==1: # 음식물 발견
            result.append(bfs(i,j, graph))

print(max(result))