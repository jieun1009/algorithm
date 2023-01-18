n = int(input())

arr = list(map(int, input().split()))

arr.sort()

total =0
for i in range(n,0,-1):
    total += arr[n-i]*i

    
print(total)