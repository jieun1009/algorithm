a = int(input())
b = int(input())
n = int(input())

answer = 0
while True:
    answer += (n//a)*b
    n = (n//a)*b + (n % a) 
    if n < a:
        break
    print(answer)
    
print(answer)