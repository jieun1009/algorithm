n = int(input())
arr = list(map(int, input().split()))

result = [0]

for i in arr:
    if result[-1]< i: # 증가하므로 삽입
        result.append(i)
    else: #중간에 삽입
        start = 0
        end = len(result)
        while start < end:
            mid = (start + end) //2

            if result[mid] < i:
                start = mid+1
            else:
                end = mid

        result[end] = i

print(len(result)-1)
