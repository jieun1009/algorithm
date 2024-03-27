h,w= map(int,input().split())
walls = list(map(int, input().split()))

top  =0
answer = 0
wallleft = walls[0]
wallright = walls[-1]


for i in range(1,len(walls)-1):
    left = max(walls[:i])
    right = max(walls[i+1:])
    wall = min(left, right)
    if walls[i] < wall:
        answer += wall - walls[i]


print(answer)