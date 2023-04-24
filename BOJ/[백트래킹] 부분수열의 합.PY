n,s = map(int, input().split())
arr = list(map(int,input().split()))
count = 0
result = []
def dfs(index):
    global count
    if sum(result)==s and len(result)>0:
        count+=1
    for i in range(index, n):
        result.append(arr[i])
        dfs(index+1)
        result.pop()
    
dfs(0)

print(count)