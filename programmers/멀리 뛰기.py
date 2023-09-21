import math
def solution(n):
    answer = 0

    # 2가 한번 있을때마다 1,1 & 2로 할수 있으므로 2개 방법 더 들어남
    two = n//2 
    if two>=1:
        answer += 1 #최대 2와 1로 표현 ex) 2,2,1
    if n%2 ==0:
        one=0
    else: one=1 
        
    # 중복순열..?
    while(two>0):
        length = two + one # 표현하는 길이  ex) 2221이면 길이 4
        #여기서 중복순열 팩토리얼 계산
        answer += math.factorial(length)//(math.factorial(two)*math.factorial(one))
        two -= 1
        one += 2
        
        

    if n==1:
        return 1
    return answer % 1234567