def solution(lottos, win_nums):
    
    # 최고순위 : 0이 다 겹칠때
    # 최저순위 : 0이 다 틀릴때
    answer = [0]*2
    count = 0
    # 일단 최소 겹치는 수 = count

    for i in range(len(win_nums)):
        if win_nums[i] in lottos: 
            count+=1
            
    if count>1:
        answer[1] = 7-count
    else: answer[1] = 6
    
    zero = lottos.count(0) 
    count += zero
    if count > 0:
        answer[0] = 7-count
    else:
        answer[0] = 6
    
    return answer