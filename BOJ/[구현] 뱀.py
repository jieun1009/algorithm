from collections import deque
n = int(input())

arr = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 2 # 사과

l = int(input())
move = {}
for _ in range(l):
    a,b = input().split()
    move[int(a)] = b

dx = [0,1,0,-1] # 각각 오른쪽, 아래, 왼쪽, 위 방향으로의 x좌표 이동량
dy = [1,0,-1,0] # 각각 오른쪽, 아래, 왼쪽, 위 방향으로의 y좌표 이동량
# x,y에서 0,0이 0,1 을 가기 위해서는 x=0, y+=1해야 함

direction = 0
def turn(cnt):  
    global direction
    if move[cnt] =="L":
        direction = (direction-1)%4 # 반시계방향으로 가기 위해선 -1
    elif move[cnt]=="D":
        direction = (direction+1)%4 # 시계방향으로 가기 위해선 +1
 
queue = deque()
queue.append((0,0)) # 뱀 첫 위치
x = 0
y = 0
arr[x][y] = 1

cnt = 0
while True:
    cnt +=1
    x += dx[direction]
    y += dy[direction]


    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if arr[x][y] == 2: # 사과가 있다면
        queue.append((x, y))  # 머리추가
        arr[x][y] = 1

    elif arr[x][y] ==0: # 사과가 없다면
        queue.append((x, y))  #머리 추가
        tx, ty = queue.popleft() # 꼬리 제거
        arr[x][y] = 1
        arr[tx][ty] = 0
    
    else:
        break

    if cnt in move: # 방향전환
        turn(cnt)

print(cnt)