
import sys


n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start =0
cnt =0
result = []
result.append(sum(arr[start:start+k]))
while start+k<n:
    result.append(result[-1] - arr[start] + arr[start+k])
    start +=1

print(max(result))