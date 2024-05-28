from collections import deque
import sys

n = int(input())
m = int(input())
city = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    city[i].append(i) # 자기 자신도 추가해야 함!!
    for j in range(n):
        if temp[j] ==1:
            city[i].append(j)

route = list(map(int, input().split()))
route = [i-1 for i in route]
visited = [False]*len(city)


q = deque()
q.append(route[0]) # 첫번째 여행지 추가

while q:
    now = q.popleft()

    for i in city[now]:

        if visited[i] == False:
            q.append(i)
            visited[i]= True # 방문!


# visited 확인 후 다 방문했는지 확인
for i in route:
    if visited[i]== False:
        print("NO")
        sys.exit(0)

print("YES")