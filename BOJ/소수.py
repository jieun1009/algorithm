M = int(input())
N = int(input())
arr = []
not_sosu=[]

for i in range(M, N+1):
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                not_sosu.append(i)
                break
        if (i not in not_sosu):
            arr.append(i)
            
if len(arr)==0:
    print(-1)         
else:
    print(sum(arr))
    print(min(arr))