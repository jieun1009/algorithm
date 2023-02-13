n = int(input())
m = int(input())

arr = sorted(list(map(int,input().split())))

start = 0
end = n-1
count = 0

while start < end:
    result = arr[start] + arr[end]
    
    if result < m : # 원하는 값보다 작음 값 늘림
        start +=1
    elif result ==m :
        count +=1
        start += 1
    else: # 원하는 값보다 큼 값 줄임
        end -= 1
        
print(count)     
