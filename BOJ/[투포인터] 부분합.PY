import sys

n,s = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

min_value = n+1

start = 0
end = 0
result = arr[0]
while start <= end:
    # temp = arr[start:end]
    # result = sum(temp)

    if result >= s : 
        min_value = min(min_value, end-start+1)
        result -= arr[start]
        start += 1
    else: 
        end += 1
        if end < n:
            result += arr[end]
        else: break
        
if min_value == n+1:
    print(0)
else : 
    print(min_value)