def solution(n, lost, reserve):
    answer = 0
    new_lost = [i for i in lost if i not in reserve]
    new_reserve = [i for i in reserve if i not in lost]
    
    new_lost.sort()
    new_reserve.sort()
    
    
    for i in new_reserve:
        if i==1 and 2 in new_lost:
            new_lost.remove(2)
        elif i>1:
            if i-1 in new_lost:
                new_lost.remove(i-1)
            elif i+1 in new_lost:
                new_lost.remove(i+1)
    
    answer = n-len(new_lost)
    return answer

lost =[2,4]
reserve=[3]

print(solution(5, lost, reserve))