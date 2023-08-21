def solution(wallpaper):
    # . 빈칸 # 파일
    answer = []
    w = len(wallpaper[0])
    h = len(wallpaper)
    # 맨 왼쪽거에서 맨 위쪽거로 이동
    # 맨 오른쪽에서 맨 아래쪽으로 이동
    min_l = w
    max_r = 0
    for i in range(0,w):
        for j in wallpaper:
            if j[i] =='#':
                min_l = min(min_l,i)
                max_r = max(max_r,i)
            
    min_h = h
    max_l = 0
      
    for idx,i in enumerate(wallpaper):
        if "#" in i:
            min_h = min(min_h,idx)
            max_l = max(max_l,idx)

    answer = [min_h, min_l,max_l+1,max_r+1]
    
    
    
    
    return answer