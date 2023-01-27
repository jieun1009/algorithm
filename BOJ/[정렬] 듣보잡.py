import sys
n,m=map(int,input().split())

arr=set()
for _ in range(n):
    arr.add(input())
    
arr2=set()
for _ in range(m):
    arr2.add(input())
    


result = sorted(list(arr&arr2))

# print(result)

print(len(result))        
for i in result:
    print(i)
    
