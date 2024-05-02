from collections import deque
import sys

r,c = map(int,input().split())
graph = []*r
human = [[0]*c for _ in range(r)]
fire = [[0]*c for _ in range(r)]

hq = deque() # 지훈용 deque
fq = deque() # 불용 deque
for i in range(r):
    graph.append(list(input())) # #:벽, .:지나갈 수 있음, J:초기 위치, F: 불난 위치
    for j in range(c):
        if graph[i][j]=="J":
            hq.append((i,j))
            human[i][j] = 1
        if graph[i][j] =="F":
            fq.append((i,j))
            fire[i][j]=1



dx = [0,1,0,-1]
dy = [1,0,-1,0]


# 불도 상하좌우 퍼지고(n개), 지훈이도 이동
def hbfs():
    while hq:
        x,y = hq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                print(human[x][y])
                return
            
            if graph[nx][ny]=='#': 
                continue

            if fire[nx][ny] and human[x][y]+1 >= fire[nx][ny]: # nx, ny에 불이 있고, 자신이 이동한 거리가 불이 도달한 거리(시간)보다 작다면 이동 불가 == 내가 가기 전에 불이 이미 퍼졌다면
                continue

            hq.append((nx,ny))
            human[nx][ny] = human[x][y]+1
    print("IMPOSSIBLE")
    return

def fbfs():
    while fq:
        x,y = fq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny]=="." and fire[nx][ny]==0:
                fire[nx][ny] = fire[x][y]+1
                fq.append((nx,ny))

fbfs()
hbfs()
