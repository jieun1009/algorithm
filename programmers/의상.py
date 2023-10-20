def solution(clothes):
    answer = 0
    cloth = dict()
    for i in clothes:
        if i[1] not in cloth :
            cloth[i[1]] =1
        else:
            cloth[i[1]]+=1
            
    temp = 1
    for i in cloth:
        temp *= ( cloth[i] +1)
    
    
    
    return temp-1