from collections import deque
import copy
from itertools import combinations
n,m  = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
safe = 0
safe_zone = []
virus_zone = []

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            safe_zone.append([i,j])
        if graph[i][j]==2:
            virus_zone.append([i,j])

# 벽세우기
def make_wall(): 
    safe_zone_combi = combinations(safe_zone, 3) # safe zone에서 3개의 위치 추출

    for wall in safe_zone_combi:
        a,b,c = wall[0], wall[1], wall[2]

        graph[a[0]][a[1]] = 1 # 벽세우기 1
        graph[b[0]][b[1]] = 1 # 벽세우기 2
        graph[c[0]][c[1]] = 1 # 벽세우기 3
        bfs()
        graph[a[0]][a[1]] = 0 # 복구
        graph[b[0]][b[1]] = 0 # 복구
        graph[c[0]][c[1]] = 0 # 복구


# 바이러스 퍼지기 
def bfs():
    global safe
    queue = deque(virus_zone)
    temp_graph  = copy.deepcopy(graph) # new
   

    bx = [-1,0,1,0]
    by = [0,-1,0,1]

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + bx[i]
            ny = y + by[i]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] =2
                queue.append((nx,ny)) # new

    temp_safe = 0
    # 0 개수 세기
    for i in temp_graph:
        temp_safe+=i.count(0)
    safe = max(safe, temp_safe)

make_wall()
print(safe)
