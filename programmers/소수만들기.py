from itertools import combinations
import math

def solution(nums):
    answer = 0
    arr = list((combinations(nums,3)))
    for i in arr:
        total = sum(i)
        for i in range(1, int(math.sqrt(total))+1):
            if i==1:
                pass
            elif total % i ==0:
                total = 0
                break  
        if total != 0:
            answer+=1

    return answer