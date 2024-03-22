from collections import deque

n,k = map(int, input().split())
queue = deque(map(int, input().split())) # 내구도
robot = deque([0]*n) # 컨베이어벨트 위의 로봇

cnt = 0
while True:
    cnt+=1

    # 벨트 회전
    queue.rotate(1) #오른쪽으로 이동
    robot[-1] = 0 # n에 있는 로봇 내림
    robot.rotate(1)
    robot[-1]=0 # 로테이트 후 n에 있는 로봇 내림

    # 로봇 이동하기
    for i in range(n-2, -1, -1): # 먼저 올라간 로봇부터 진행
        if queue[i+1] >=1 and robot[i+1] ==0 and robot[i]==1: # 이전 내구도 1이상, 이전에 로봇 없고, 현재 로봇 있고
            robot[i+1]=1
            robot[i]=0
            queue[i+1]-=1

    robot[-1] = 0 # 이동 후 n에 있는 로봇 내림

    # 1에 로봇 올리기
    if queue[0]!=0 and robot[0]!=1:
        robot[0]=1
        queue[0]-=1

    # 내구도 0인 칸이 k개 이상이면 종료
    if queue.count(0)>=k:
        break

print(cnt)