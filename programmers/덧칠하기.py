def solution(n, m, section):
    answer = 0
    index = 0
    
    for i in section:
        if index < i:
            answer += 1
            index = i + m -1
        
    return answer