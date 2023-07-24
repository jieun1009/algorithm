def solution(N, stages):
    
    answer = []
    arr = [0]*(N+1)
    etc = [0]*(N+1)
    for i in range(1,N+1):
        for j in range(len(stages)):
            if i == stages[j]:
                arr[i]+=1
                
    etc[0]=len(stages)
    
    
    for i in range(1,N+1): 
        etc[i]=(etc[i-1]-arr[i])
        if etc[i-1] !=0:
            answer.append(arr[i]/etc[i-1])
        else:
            answer.append(0)

    answer = sorted(range(len(answer)), key=lambda k:answer[k], reverse= True)
    for i in range(len(answer)):
        answer[i]+=1
    
    return answer