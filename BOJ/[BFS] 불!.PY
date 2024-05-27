from collections import deque

r,c = map(int, input().split())

arr = []*r
human = [[0]*c for _ in range(r)]
fire = [[0]*c for _ in range(r)]

bx = [0, -1, 0, 1]
by = [-1, 0, 1, 0]

fq = deque()
hq = deque()

# 사람과 불 초기 큐 값 셋팅
for i in range(r): 
    arr.append(list(input()))
    for j in range(c):
        if arr[i][j] == "J":
            hq.append((i,j))
            human[i][j] = 1
        if arr[i][j] == "F":
            fq.append((i,j))
            fire[i][j] = 1

def fbfs():
    while fq:
        x,y = fq.popleft()
        
        for i in range(4):
            nx = bx[i] + x
            ny = by[i] + y

            if nx <0 or nx >= r or ny < 0 or ny >= c:
                continue
            if arr[nx][ny] != "#" and not fire[nx][ny]: # 벽이 아니고, 불이 안번진데면(fire==0) 불 번짐
                fire[nx][ny]= fire[x][y]+1
                fq.append((nx, ny))


def hbfs(): 
    while hq:
        x,y = hq.popleft()
        for i in range(4):
            nx = bx[i] + x
            ny = by[i] + y

            if nx <0 or nx >= r or ny < 0 or ny >= c: # 벽 통과 == 성공
                print(human[x][y])
                return
            
            if arr[nx][ny]=="#" or human[nx][ny]: # 벽이거나 human[nx][ny]==1(이미 방문했으면)
                continue

            # 불이 있고(불이 아예 없으면 사람은 이동해도 됨 but 1이라도 있으면 이동 불가), 불이 이미 먼저 번진 경우
            if fire[nx][ny] and fire[nx][ny] <= human[x][y]+1: 
                continue    
                
            hq.append((nx, ny))
            human[nx][ny] = human[x][y]+1

    print("IMPOSSIBLE")
    return 


fbfs()
hbfs()
