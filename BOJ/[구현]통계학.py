from collections import Counter
import sys

n = int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(round(sum(arr)/n))
print(arr[n//2])

most_arr = Counter(arr).most_common(2)

if len(most_arr)>1:
    if most_arr[0][1]==most_arr[1][1]:
        print(most_arr[1][0])
    else:
        print(most_arr[0][0])
else:
    print(most_arr[0][0])

print(arr[n-1] - arr[0])