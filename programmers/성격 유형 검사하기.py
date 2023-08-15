def solution(survey, choices):
    # 매우 3 그냥 2 약간 1 모름 0
    grade = [3,2,1,0,1,2,3]
    arr={"R":0, "T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    answer = ''
    for idx, i in enumerate(survey):
        if choices[idx]<4:
            arr[i[0]] += grade[choices[idx]-1]

        elif choices[idx]>4:
            arr[i[1]] += grade[choices[idx]-1]

    pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]

    for i, j in pairs:
        if arr[i] < arr[j]: 
            answer += j
        else:
            answer += i
    
    return answer