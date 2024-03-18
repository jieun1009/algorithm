from collections import deque

n, k = map(int, input().split())
max = 100000
visited = [0]*(max+1)
cnt = 0
def bfs(x):
    global cnt
    queue = deque()
    queue.append(x)

    while queue:
        a = queue.popleft()
        
        if a==k:
            cnt+=1
        else:
            for i in (a-1, a+1, 2*a):
                if 0<=i<=max:
                    if visited[i]==0 or visited[i] >= visited[a]+1: # 방문 안했거나, 방문했어도 현재 횟수보다 더 많거나 같으면 교체
                        queue.append(i)
                        visited[i] = visited[a]+1

bfs(n)
print(visited[k])
print(cnt)