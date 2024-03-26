from collections import deque

n, l, r = map(int,input().split())

country = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]



# 인접 국가 찾기
def bfs(i,j):
    q = deque()
    q.append((i,j))
    union = [(i,j)]
    visited[i][j]= 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            move=True

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(country[nx][ny] - country[x][y]) <= r:
                    q.append((nx,ny))
                    union.append((nx,ny))
                    visited[nx][ny]=1
                    
                    
    return union



cnt = 0
while True : 

    visited = [[0]*n for _ in range(n)]
    move = False
    
    # 인접 국가 찾기
    for x in range(n):
        for y in range(n):
            if visited[x][y]==0:
                union = bfs(x,y)
        
                # 인구 이동
                if len(union) > 1:
                    move = True
                    people = sum(country[i][j] for  i,j in union) // len(union)

                    for i, j in union:
                        country[i][j] = people

    if move == False:
        break
    cnt +=1

print(cnt)