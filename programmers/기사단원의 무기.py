import math
def solution(number, limit, power):
    answer = 0
    result = [0]*(number) # 각 단원들이 살 최종 무기
    
    # 각 기사별(0~number) 약수 개수 알아내기
    for i in range(1,number+1):
        count = 0
        
        for j in range(1,int(math.sqrt(i))+1): 
            if i%j == 0: # 약수임
                count +=1
                
        if i!=1:
            if int(math.sqrt(i)) * int(math.sqrt(i)) ==i : # 제곱수이면

                result[i-1] += (count-1) *2
                result[i-1] += 1
            else:
                result[i-1] += count*2
        else:
            result[i-1] += count    
            
    
    # 약수 개수가 limit 넘는지 확인 -> 넘으면 power값으로 변경
    for i in range(len(result)):
        if result[i] > limit: 
            result[i] = power
            
    
    # result 다 더하기
    answer = sum(result)
    
    return answer