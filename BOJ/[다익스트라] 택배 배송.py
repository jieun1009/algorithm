import heapq
n,m = map(int, input().split())

INF = int(1e9)

cow = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    cow[a].append((b,c))
    cow[b].append((a,c))

distance = [INF]*(n+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로(가중치 =0)
    distance[start] =0
    
    while q:

        dist , now = heapq.heappop(q) # 가중치, 현재 위치 꺼내기
        
        if distance[now] < dist: # 만약 현재 위치의 가중치가 이미 더 작다면 패스
            continue


        for i in cow[now]: # now 에서 연결된 다른 곳(i)으로 가기
      
            cost = dist + i[1] # i 까지의 가중치 = now까지의 가중치 + now에서 i까지의 가중치
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
print(distance[n])