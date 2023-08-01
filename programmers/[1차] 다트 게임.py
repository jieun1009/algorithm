def solution(dartResult):
    # 숫자 제곱수 옵션 * 앞, 현재 2배 # 해당 점수 마이너스
    answer = []
    result = []
    sdt = ['S','D','T']
    dartResult = dartResult.replace('10','k')
    result = ['10' if i =='k' else i for i in dartResult]
    
    for i in result:
        if i in sdt:
            answer[-1] = answer[-1] ** (sdt.index(i)+1) # 제곱/세제곱
        elif i == '*':
            answer[-1]*= 2
            if len(answer)>1:
                answer[-2]*= 2
                
        elif i =='#':
            answer[-1]*= -1
        else:
            answer.append(int(i))
            

    
    return sum(answer)