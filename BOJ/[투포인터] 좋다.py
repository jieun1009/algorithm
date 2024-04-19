n = int(input())
num = list(map(int,input().split()))

num.sort()


cnt = 0
for i in range(n):
    
    arr = num[:i]+num[i+1:] # 자기 자신 제외한 다른 두 수의 합이어야 함
    start = 0
    end = len(arr)-1
    while start < end:
        temp = arr[start] + arr[end]
        if temp == num[i]:
            cnt+=1
            break

        if temp < num[i]:
            start += 1
        else:
            end -= 1

print(cnt)