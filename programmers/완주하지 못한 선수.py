def solution(participant, completion):
     
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i] # 동명이인 있으면 달라지는 순간 해당 사람
    return participant[len(participant)-1] # 동명이인 없으면 마지막이 미완