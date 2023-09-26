from collections import Counter

def solution(k, tangerine):
    answer = 0
    result = 0 
    arr= Counter(tangerine).most_common()
    # print(arr)
    for key, value in arr:
        result += value
        answer +=1
        if result>=k:
            break
            
    return answer