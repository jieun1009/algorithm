def solution(n):
    answer = 1
    
    # 2개의 수로 표현부터 시작
    for i in range(2,int(n/2)+2):
        sum_val = sum(range(1,i))
        if sum_val> n:
            break
        temp = n-sum_val
        
        if temp > 0 and temp %i==0:
            answer+=1
    

    return answer