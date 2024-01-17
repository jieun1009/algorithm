def solution(priorities, location): 
    queue = [(i,p) for i,p in enumerate(priorities)] # 큐 구현(idx, priorities 값)
    answer = 0
    while True:
        now = queue.pop(0)
        if any(now[1] < q[1] for q in queue):
            queue.append(now) # queue 중에 하나라도 자기보다 큰게 있으면 다시 큐에 넣기
        else: # 본인이 제일 크다면 = 큐에서 방출
            answer +=1 # 가장 큰 순으로 순위 정해짐
            if now[0] == location: # 원하는 프로세스일 경우
                return answer # 리턴