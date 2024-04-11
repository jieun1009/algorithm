def isConnect(tictacto, x):
    # 가로 판별
    if tictacto[0][0]==tictacto[0][1]==tictacto[0][2]==x:
        return True
    if tictacto[1][0]==tictacto[1][1]==tictacto[1][2]==x:
        return True
    if tictacto[2][0]==tictacto[2][1]==tictacto[2][2]==x:
        return True
    # 세로 판별
    if tictacto[0][0]==tictacto[1][0]==tictacto[2][0]==x:
        return True
    if tictacto[0][1]==tictacto[1][1]==tictacto[2][1]==x:
        return True
    if tictacto[0][2]==tictacto[1][2]==tictacto[2][2]==x:
        return True
    # 대각선 판별
    if tictacto[0][0]==tictacto[1][1]==tictacto[2][2]==x:
        return True
    if tictacto[0][2]==tictacto[1][1]==tictacto[2][0]==x:
        return True
    return False

while True:
    text = input()
    if text=="end":
        break

    tictacto = [[0]*3 for _ in range(3)]
    idx = 0
    xcnt = 0
    ocnt = 0
    for i in range(3):
        for j in range(3):
            tictacto[i][j] = text[idx]
            idx+=1

    xcnt = text.count("X")
    ocnt = text.count("O")

    if xcnt>ocnt+1:
        print("invalid")
        continue
    if ocnt>xcnt:
        print("invalid")
        continue
    if ocnt==xcnt: # o가 이기는 경우
        if isConnect(tictacto,"O") and not isConnect(tictacto,"X"):
            print("valid")
            continue
    if xcnt==ocnt+1:
        if isConnect(tictacto,"X") and not isConnect(tictacto,"O"):
            print("valid")
            continue
    if xcnt==5 and ocnt==4:
        if not isConnect(tictacto,"O"):
            print("valid")
            continue
    
    print("invalid")