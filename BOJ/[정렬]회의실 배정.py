n = int(input())

arr = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
    
arr.sort(key=lambda x:(x[1],x[0]))

result = []
result.append(arr[0])
for i in range(1,len(arr)):
    if result[-1][1] <= arr[i][0]:
        result.append(arr[i])

print(len(result))