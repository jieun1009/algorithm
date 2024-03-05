import sys
sys.setrecursionlimit(10**6)

n = int(input())

drawing = [input() for i in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]



def dfs(x,y,normal):
    visited[x][y] = True # 방문

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
   
        if nx < 0 or nx >= n or ny < 0 or ny >= n: # 범위 벗어나는 경우
            continue
        
        if visited[nx][ny] == False : # 방문 안한 경우 방문!

            if normal == True and drawing[x][y]==drawing[nx][ny]: # 아닌사람의 경우 같은 색깔 방문
                dfs(nx, ny, normal)

            elif normal == False :
                if drawing[x][y] == "B" and drawing[nx][ny] =="B": # 현재 파랑이면 파랑만 방문
                    dfs(nx, ny, normal)
                elif drawing[x][y] != "B" and drawing[nx][ny] !="B": # 현재 파랑 아니면(빨, 초), 파랑 아닌 것 방문
                    dfs(nx, ny, normal)



visited = [[False]*n for i in range(n)]
normal = 0
for i in range(n):
    for j in range(n):
            if visited[i][j]==False:
                dfs(i,j,True)
                normal+=1


visited = [[False]*n for i in range(n)]
redgreen = 0
for i in range(n):
    for j in range(n):
            if visited[i][j]==False:
                dfs(i,j,False)
                redgreen+=1


print(normal, redgreen)