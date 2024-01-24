import math
def solution(n, k):
    answer = -1
    
    # 진수 변환
    num = ""
    while True:
        if n <= k:
            mod = n%k
            num = str(mod) +num
            break
        
        mod = n % k
        n //= k
        num = str(mod) + num
    
    # 0 제거 
    prime_arr = []
    primenum = ""
    for i in num:
        if i!="0":
            primenum += i
        else:
            if primenum!="" and primenum!="1": prime_arr.append(primenum)
            primenum = ""
    if primenum!="" and primenum!="1": prime_arr.append(primenum)

    answer = len(prime_arr)
    # 소수 판별
    for i in prime_arr:
        for j in range(2,int(math.sqrt(int(i))+1)):
            if int(i) % j==0:
                answer-=1
                break
    
    
    return answer