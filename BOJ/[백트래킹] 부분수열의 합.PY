n,s = map(int, input().split())
arr = list(map(int,input().split()))

result = []
count = 0
def dfs(index):
    global count
    if sum(result)==s and len(result)>0:
        count +=1
    for i in range(index, n):
        result.append(arr[i])
        dfs(i+1)
        result.pop()

dfs(0)
print(count)