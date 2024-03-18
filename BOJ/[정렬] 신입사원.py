import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        s, m = map(int, sys.stdin.readline().split())
        arr.append((s,m))

    arr.sort(key = lambda x: x[0])
    cnt =1
    rank = arr[0][i] # 서류 1등이 기준
    for i in range(n):
        if arr[i][1] < rank : # 면접 등수가 이전 사람보다 높으면(arr은 서류 기준으로 정렬)
            cnt+=1
            rank = arr[i][1]

    print(cnt)