from collections import deque


n = int(input())
visited = [False]*(n+1)
arr = [[] for _ in range(n+1)]
result = [0]*(n+1)

for _ in range(n-1):
    s,d = map(int,input().split())
    arr[s].append(d)
    arr[d].append(s)
    
def bfs(arr, v, visited):
    q = deque([v])
    visited[v]=True
    while q:
        v = q.popleft()
        
        for i in arr[v]:
            if not visited[i]:
                result[i]=v # i의 직전 노드 v가 부모임
                q.append(i)
                visited[i]=True
        
        
bfs(arr, 1, visited)
for i in range(2, n+1):
    print(result[i])