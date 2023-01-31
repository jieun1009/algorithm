n = int(input())
arr = list(map(int,input().split()))
m = int(input())

start , end = 0, max(arr)
while start <= end:
    total = 0 # 총 지출양
    mid = (start + end) //2
    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i
            
    if total <= m: # 지출 양이 예산보다 작으면
        start = mid+1
    else:
        end = mid -1
            
print(end)
    

