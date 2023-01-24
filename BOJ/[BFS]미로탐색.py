from collections import deque

n,m = map(int,input().split())

graph =[]

for i in range(n):
    graph.append(list(map(int,input())))

bx = [0,1,0,-1]
by = [1,0,-1,0]

q = deque()
q.append((0,0))

count = 1

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+bx[i]
        ny = y+by[i]

        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        
        if graph[nx][ny]==1:
            graph[nx][ny] = graph[x][y]+1 # 그래프 여태까지 방문한거 +1
            q.append((nx,ny))
            
print(graph[n-1][m-1])
