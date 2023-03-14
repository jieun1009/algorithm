from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
    
bx = [0,1,0,-1]
by = [1,0,-1,0]
graph[0][0]=1

def bfs(x,y):
    queue = deque()
    queue.append((x,y,1))
    visit = [[[0]*2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1 # 1이면 벽뚫기 가능, 0이면 이미 뚫음
    
    while queue:
        x,y,w = queue.popleft()
        
        if x==n-1 and y==m-1:
            return visit[x][y][w]
        
        for i in range(4):
            nx = x + bx[i]
            ny = y + by[i]
            
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            
            if graph[nx][ny]==1 and w==1: # 벽뚫기 가능하고 1이면
                visit[nx][ny][0] = visit[x][y][1] + 1
                queue.append((nx,ny,0))
    
            elif graph[nx][ny]==0 and visit[nx][ny][w] == 0: #벽뚫기 불가능하고 처음 방문
                visit[nx][ny][w] = visit[x][y][w] + 1
                queue.append((nx,ny,w))
                
    return -1
            
    
print(bfs(0,0))     
