t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        s, m = map(int, input().split())
        arr.append((s,m))

    arr.sort(key = lambda x: x[0])

    answer = 1
    answerarr = []
    maxvalue = 0
    for i in range(n-1):
        maxvalue = max(maxvalue, arr[i][1])
        if maxvalue > arr[i+1][1]:
            answer +=1
        else:
            answerarr.append(answer)
            answer = 1
    answerarr.append(answer)
    print(max(answerarr))