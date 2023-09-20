import math
from fractions import gcd

def solution(arr):
    answer = 0
    # a * b = 최대공약수 * 최소공배수
		#여러수의 최소공배수 = a,b의 최소공배수 & c의 최소공배수 = a,b,c의 최소공배
    
    temp=[arr[0]]
    total = math.prod(arr)

    while(len(arr)>0):
        a= temp.pop()
        b= arr.pop()
        
        lcm = a*b / gcd(a,b) #최대공약수 구하기
        temp.append(lcm)
        
                    
    return temp[0]