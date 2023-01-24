from collections import deque

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
    
bx = [1,0,-1,0]
by = [0,1,0,-1]

q = deque()
count = 1
def bfs(x,y):
    q.append((x,y))
    graph[x][y]=0
    
    global count 
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + bx[i]
            ny = y + by[i]
            
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
        
            if graph[nx][ny]==1:
                count +=1
                graph[nx][ny]=0
                q.append((nx,ny))
   
cntlist =[]  
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)
            cntlist.append(count)
            count = 1

print(len(cntlist))
cntlist.sort()
for i in range(len(cntlist)):
    print(cntlist[i])