from collections import deque

max = 100001
n, k = map(int, input().split())
visited = [0]*max
cnt = [0]*max

def bfs(start):
    queue = deque()
    queue.append(start)
  
    while queue:
        x = queue.popleft()

        if x == k:
            return cnt[x]

        for i in (x+1, x-1, 2*x):
            if 0<=i<max and visited[i]==0:
                queue.appendleft(i)
                visited[i]=1
                if i==2*x:
                    cnt[i] = cnt[x]
                elif i==x-1:
                    cnt[i] = cnt[x]+1
                elif i==x+1:
                    cnt[i] = cnt[x]+1



print(bfs(n))