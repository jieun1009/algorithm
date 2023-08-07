def solution(keymap, targets):
    answer = []
    # 여러개의 키에 동일 값이 있는 경우 더 빠른 것 get
    for i in targets: # 만들 문자열
        count = 0
        for alpha in i: # 각 문자
            minCnt = 101
            for key in keymap:
                if alpha in key:
                    idx = key.index(alpha)+1
                    minCnt = min(minCnt,idx)      
                if key == keymap[-1] and minCnt ==101:
                    break
            if minCnt!= 101:
                count += minCnt
            else:
                count = -1
                break
        if count != -1:
            answer.append(count)
        else:
            answer.append(-1)

    return answer