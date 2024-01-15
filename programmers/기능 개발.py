import math
def solution(progresses, speeds):
    answer = []
    
    days_arr = []
    for index, i in enumerate(progresses):
        days = math.ceil((100-i)/speeds[index])
        days_arr.append(days)

    
    max_value = days_arr[0]
    process =1

    for i in range(1, len(days_arr)):
        print(max_value, days_arr[i])
        if max_value < days_arr[i]:
            max_value = days_arr[i]
            answer.append(process)
            process=1
            
        else:
            process+=1
    answer.append(process)
    
    
    return answer