from collections import deque

t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    arr = deque(input()[1:-1].split(","))
    flag = 0
    if n == 0:
        arr = deque()
    
    rcnt = 0
    for i in range(len(p)):
        if p[i] == "R":
            rcnt += 1
        else:
            if len(arr) == 0:
                print("error")
                flag = 1
                break
            else:
                if rcnt %2 ==0:
                    arr.popleft()
                else:
                    arr.pop()
    if flag ==1:
        continue

    else:
        if rcnt %2 ==0:
            print('[' + ",".join(arr) + ']')

        else:
            arr.reverse()
            print('[' + ",".join(arr) + ']')

    
