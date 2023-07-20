def solution(answers):
    # answers = [1,2,3,4,5,1,2,3,2,3,4]
    # 1번 : 12345 / 2번: 21232425 / 3번: 3311224455
    fir = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    
    answer = []
    
    cnt = [0,0,0]
 
    for i in range(len(answers)):
        idx = [i % len(fir), i % len(sec), i % len(thr)]
        
    
        if answers[i] == fir[idx[0]]:
            cnt[0] +=1
        if answers[i] == sec[idx[1]]:
            cnt[1] +=1
        if answers[i] == thr[idx[2]]:
            cnt[2] +=1
    
    

    answer = list(filter(lambda e:(cnt[e] == max(cnt)), range(len(cnt)))) 
    answer = [i+1 for i in answer]

    
    return answer