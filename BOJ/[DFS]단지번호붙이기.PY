n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
    
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def dfs(x,y):
    graph[x][y]=0
    global cnt
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue
        
        if graph[nx][ny]==1:
            cnt +=1
            dfs(nx,ny) 

cnt = 0
cntlist = []
totalcnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            dfs(i,j)
            cntlist.append(cnt)
            cnt = 0
    
            
print(len(cntlist))
cntlist.sort()
for i in range(len(cntlist)):
    print(cntlist[i])
