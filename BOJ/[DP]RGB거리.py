n =  int(input())

arr =[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
    # 0 빨 1 초 2 파

for i in range(1, n):
    # 빨간집을 선택한 경우 : 이전 선택이 초/파
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    # 초록집 : 이전 선택이 빨/파
    arr[i][1] = min(arr[i-1][0], arr[i-1][2])+arr[i][1]
    # 파란집
    arr[i][2] = min(arr[i-1][0], arr[i-1][1])+arr[i][2]
    
print(min(arr[n-1]))