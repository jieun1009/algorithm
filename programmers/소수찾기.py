import math
def is_prime_number(x):
    for j in range(2, int(math.sqrt(x))+1):
        if x%j==0:
            return False
    return True

def solution(n):
    answer = 0
    flag = False
    
    for i in range(2, n+1):
        if is_prime_number(i):
            answer+=1
            
    return answer