from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([0,numbers[0]])
    queue.append([0,-1*numbers[0]])
    
    while(queue):
            index, value = queue.pop()
            index+= 1
            if (index == len(numbers) and value==target):
                answer += 1
            if index < len(numbers):
                queue.append([index, value+numbers[index]])
                queue.append([index, value-numbers[index]])
                
                
    return answer