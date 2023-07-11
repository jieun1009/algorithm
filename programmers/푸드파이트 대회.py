def solution(food):
    # 0=물 1~=음식(칼로리적은 순)
    arr = []
    for i in range(1,len(food)):
        num = food[i]//2
        for j in range(num):
            arr.append(i)
            
    rever = list(reversed(arr))
    arr.append(0)
    arr = arr + rever


    answer = ''.join(str(i) for i in arr)
    return answer