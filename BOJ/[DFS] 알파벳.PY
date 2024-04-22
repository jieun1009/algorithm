r,c = map(int, input().split())

visited = [0]*26

alpha = []
for _ in range(r):
    alpha.append(list(input()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

maxcnt = 0
def dfs(x, y, cnt):
    visited[ord(alpha[x][y])-65] = 1 # 해당 알파벳 방문처리
    global maxcnt
    maxcnt = max(cnt, maxcnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
            
        if visited[ord(alpha[nx][ny])-65]==0: # 방문 안한 알파벳이면 방문
            visited[ord(alpha[nx][ny])-65]=1 # 방문처리
            dfs(nx, ny, cnt+1)
            visited[ord(alpha[nx][ny])-65]=0 # 방문 취소
 

dfs(0,0,1)
print(maxcnt)