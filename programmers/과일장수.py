def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    total = []
    arr = []
    for i in score:
        
        arr.append(i)
        
        if len(arr) >= m:
            total.append(arr)
            arr = []
            
    price = 0
    for i in total:
        i.sort()
        price += i[0] * m
    
    return price