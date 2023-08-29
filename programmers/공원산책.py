def solution(park, routes):
    # N: 위 S: 아래 W:왼 E:오
    answer = []
    
    #시작지점 찾기
    for h in range(len(park)):
        for w in range(len(park[h])):
            if park[h][w]=="S":
                startH =h
                startW =w
                
    print("시작: ",startH, startW)
    # 이동 
    h = len(park) # 세로 길이
    w = len(park[0]) # 가로길이
    
    #시작위치에서 시작
    nowH = startH
    nowW = startW 
    for i in routes:
        route = i.split(" ")
        direct = route[0]
        distance = int(route[1])
        print(i)

        # 위 아래면 H
        if direct=="N" or direct =="S":
            
            tempP = nowH+distance
            tempM = nowH-distance
            if direct=="N" and 0<=tempM<=h-1 :
                for i in range(1, distance+1):
                    temp = nowH-i
                    if "X" == park[temp][nowW]:
                        break
                    if temp == nowH-distance:
                        nowH-=distance  
                        
            elif direct=="S" and 0<=tempP<=h-1 :
                for i in range(1, distance+1):
                    temp = nowH+i
                    if "X" == park[temp][nowW]:
                        break
                    if temp == nowH+distance:
                        nowH+=distance
                
        # 왼오른이면 W  
        if direct=="W" or direct =="E":
            tempP = nowW+distance
            tempM = nowW-distance
            if direct=="E" and 0<=tempP<=w-1 :
                for i in range(1, distance+1):
                    temp = nowW+i
                    if "X" == park[nowH][temp]:
                        break
                    if temp == nowW+distance:
                        nowW+=distance

                
            if direct=="W" and 0<=tempM<=w-1 :
                # 한칸씩 이동하며 장애물 확인
                
                for i in range(1, distance+1):
                    temp = nowW-i
                    if "X" == park[nowH][temp]:
                        break
                    if temp == nowW-distance:
                        nowW-=distance
                    

    
    return [nowH,nowW]