def solution(s):
    arr = list(s)
    x = s[0]
    answer = 0
    x_cnt = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == x:
            x_cnt +=1
        else:
            cnt +=1
            
        if x_cnt == cnt:
            answer += 1
            x_cnt = 0
            cnt = 0
            if i!=len(arr)-1:
                x = arr[i+1]
                
        if i==len(arr)-1 and x_cnt !=cnt:
            answer+=1
    
    
    return answer