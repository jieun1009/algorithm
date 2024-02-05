def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]: # 뒷 큰수를 못찾은 numbers이 값과 현재 numbers 값 비교
            # 더 크다면
            answer[stack.pop()] = numbers[i] # answer값을 뒷 큰수 값으로 변경
        stack.append(i) # 현재 인덱스 추가
    
    
    return answer