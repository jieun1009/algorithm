def solution(s):
    
    arr = list(s)
    result = [-1]*len(arr)
    alpha = [-1]*26
    # 최근에 나온 index 기록?
    
    for i in range(len(arr)): #한글자씩 돌아가며
        num = ord(arr[i])-97
        
        # 첫 글자일때
        if alpha[num] == -1:
            alpha[num] = i # 현재 인덱스 넣음
        else:
            # alpha[num]엔 마지막 인덱스 기록됨
            # 현재 6번째인데, 4번째에 가장 가까우면

            result[i] = (i-alpha[num])
            alpha[num] = i
    
    
    return result