def solution(scoville, K):
    answer = 0
    
    while True:
        scoville.sort()
        if scoville[0] >= K :
            return answer
        if len(scoville) < 4 and scoville[-1] + scoville[-2]*2 < K:
        # if len(scoville)==1 and scoville[0]<K:
				# if (scoville[-1] + scoville[-2]*2)*(length-1) <= K:
            return -1
        
        answer+=1
        one = scoville.pop(0)
        two = scoville.pop(0)
        scoville.append(one+two*2)
    
    return answer