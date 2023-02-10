n,m = map(int,input().split())

arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

start = 0
start2 = 0

result = []
    
while start != n or start2 != m:
    if start == n: # arr 포인터가 끝에 갔다면 arr2를 추가함
        result.append(arr2[start2])
        start2 += 1
    elif start2 ==m : # arr2 포인터가 끝에 갔다면 arr을 추가함
        result.append(arr[start])
        start += 1
    else: # 둘다 끝이 아니면 둘중 비교해서 더 작은 값 추가(정렬 필요없게 됨)
        if arr[start] < arr2[start2]:
            result.append(arr[start])
            start += 1
        else:
            result.append(arr2[start2])
            start2 += 1
            

print(*result)