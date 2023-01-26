import sys
sys.setrecursionlimit(10000)

n,m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


visited=[False]*(n+1)

def dfs(x):
    visited[x]=True
    
    # print(x, graph[x])
    for i in graph[x]:

        if not visited[i]:
            dfs(i)

count = 0           
for i in range(1,n+1):
    if not visited[i]:
        if not graph[i]:
            count +=1
            visited[i]= True
        else:
            dfs(i)
            count+=1
        
print(count)