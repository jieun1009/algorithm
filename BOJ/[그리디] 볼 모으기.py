n = int(input())
arr = list(input())
answer = []

def move_balls(color, left):
    # 빨강, 왼쪽의 경우
    start = False
    cnt =0
    if left == True:
        for idx,ball in enumerate(arr):
            if ball!=color:
                start = True
                continue
            if start == True and ball==color:
                cnt +=1
        answer.append(cnt)
    else:
        temp = arr.reverse()
        for idx,ball in enumerate(arr):
            if ball!=color:
                start = True
                continue
            if start == True and ball==color:
                cnt +=1
        answer.append(cnt)

move_balls("R",True)
move_balls("R",False)
move_balls("B",True)
move_balls("B",False)

print(min(answer))


