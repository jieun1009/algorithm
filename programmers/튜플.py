def solution(s):
    answer = []

    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len) # 숫자가 적은것부터가 먼저 들어온 애들!
    
    for i in s:
        temp = i.split(",")
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer