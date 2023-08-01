from collections import Counter

def solution(X, Y):
    x= Counter(X)
    y= Counter(Y)
    result = []
    
    for i in range(10):
        if x[str(i)] > y[str(i)]:
            for j in range(y[str(i)]):
                result.append(str(i))
        else:
            for j in range(x[str(i)]):
                result.append(str(i))

    
    if len(result)==0:
        answer = "-1"
    elif sum([int(i) for i in result])==0:
        answer ="0"
    else:
        result.sort(reverse=True)
        answer = ''.join(result)
    
    
    return answer