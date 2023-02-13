n = int(input())
arr = list(map(int, input().split()))
x = int(input())

start = 0
end = n-1
arr.sort()
count =0

while start < end and end < n :
    result = arr[start]+arr[end]

    if result > x : # 원하는 값보다 큼 (값 줄임)
        end -= 1
    elif result == x :
        count +=1
        start+=1 # 다음으로 넘어감

    else: # 원하는 값보다 작음 == 값 늘림
        start += 1
        
print(count)