from collections import deque

n, k = map(int, input().split())
max = 100001
visited = [0]*max # 방문 체크
cnt = [0]*max # 방문 횟수

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        x = queue.popleft()

        if x==k:
            print(cnt[x])
            return 
        
        if 0<=2*x<max and not visited[2*x]:
            queue.appendleft(2*x)
            visited[2*x] = 1
            cnt[2*x] = cnt[x]
        if 0<=x-1<max and not visited[x-1]:
            queue.append(x-1)
            visited[x-1] = 1
            cnt[x-1] = cnt[x]+1
        if 0<=x+1<max and not visited[x+1]:
            queue.append(x+1)
            visited[x+1] = 1
            cnt[x+1] = cnt[x]+1

bfs(n)
