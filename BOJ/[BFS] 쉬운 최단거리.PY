from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

bx = [-1, 0, 1, 0]
by = [0, -1, 0, 1]
visited = [[0]*(m+1) for i in range(n+1)]
def bfs(i, j):
    
    queue = deque()
    queue.append((i,j))
    

    while queue:
        x, y = queue.popleft()
        visited[x][y]=1
        for i in range(4):
            nx = bx[i] + x
            ny = by[i] + y

            if nx <0 or nx >= n or ny<0 or ny>=m : 
                continue
            if graph[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=1
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]==1:
                graph[i][j]=-1

for i in range(n):
    for j in range(m):
        if graph[i][j]==2 and visited[i][j]==0:
            graph[i][j]=0
            bfs(i,j)
            

for i in range(n):
    print(*graph[i])