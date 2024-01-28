def solution(msg):
    answer = []
    # 사전 초기화
    lzw = {chr(i):i-64 for i in range(65,91)}

    w,c = 0,0 # 현재, 다음 인덱스 초기화
    # 사전에 있으면 w=w, c+=1
    # 사전에 없으면 w=c, c+=1
    
    
    while True:
        c+=1
        if c == len(msg): # 인덱스 끝까지 이동한 경우
            answer.append(lzw[msg[w:c]])
            break
        # if msg[w:c+1] in lzw: # 사전에 있다면
            # 다음 글자가 사전에 없을때까지 c+=1

        if msg[w:c+1] not in lzw: # 사전에 없다면
            lzw[msg[w:c+1]]=len(lzw)+1 # 사전에 추가
            answer.append(lzw[msg[w:c]])
            w=c
    
    return answer