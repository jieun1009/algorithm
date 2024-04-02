import sys

n = int(input())
arr = list(map(int, input().split()))

answer = float("INF") # 양의 무한대
left = 0
right = 0

for i in range(n-1):
    now = arr[i]

    start = i+1
    end = n-1

    while start <= end:
        mid = (start+end)//2
        temp = now + arr[mid]

        if abs(temp)<answer:
            answer= abs(temp)
            left= i
            right = mid

            if temp ==0:
                break
        if temp < 0:
            start = mid+1
        else:
            end = mid-1

print(arr[left], arr[right])