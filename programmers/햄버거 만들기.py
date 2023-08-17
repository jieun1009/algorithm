def solution(ingredient):
    # 1 빵 2 야채 3 고기 1->2->3->1
    arr = []
    answer = 0
    temp = 0
    ham = 0
    for i in range(len(ingredient)):
        arr.append(ingredient[i])
        if [1,2,3,1] == arr[-4:]:
            answer+=1
            arr.pop()
            arr.pop()
            arr.pop()
            arr.pop()
    
    return answer