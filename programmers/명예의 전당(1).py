def solution(k, score):
    result = [] # 해당 일 상위 k개
    answer = [] # 해당 일 최하위
    
    for i in score:
        if len(result) < k:
            result.append(i)
            
        else: # k개 꽉 차있음
            if i >= result[-1]:
                del result[-1]
                result.append(i)           
        
        result.sort(reverse=True)
        answer.append(result[-1])

    return answer