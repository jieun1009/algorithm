n = int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int, input().split()))) # 0 빨 1 초 2 파

for i in range(1,len(arr)):
    # 빨강 선택
    arr[i][0] = min(arr[i-1][1], arr[i-1][2])+arr[i][0]
    # 초록 선택
    arr[i][1] = min(arr[i-1][0], arr[i-1][2])+arr[i][1]
    # 파랑 선택
    arr[i][2] = min(arr[i-1][0], arr[i-1][1])+arr[i][2]
    
print(min(arr[n-1]))