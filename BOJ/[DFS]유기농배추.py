import sys
sys.setrecursionlimit(10000)
t = int(input())

arr = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y):
        
    arr[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= m or nx <0 or ny >= n or ny < 0:
            continue
        
        if arr[nx][ny] ==1:
            dfs(nx,ny)

for _ in range(t):
    count = 0

    m,n,k = map(int,input().split())

    arr = [[0]*n for i in range(m)]
    for _ in range(k):
        x,y = map(int,input().split())
        arr[x][y] = 1
        
   
    for i in range(m):
        for j in range(n):
            if arr[i][j]==1:

                count +=1
                dfs(i,j)
                
    print(count)
