import sys
import heapq
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

INF = 1e9
distance = [INF]*(v+1) # 정점
distance[k] = 0

def dijkstra(x):
    q = []
    heapq.heappush(q, (0,x)) 

    while q:
        dist, now = heapq.heappop(q) # 가중치와 현재 지점

        if dist > distance[now]: # 가중치가 더 크면 무시
            continue
        for i in graph[now]: # 현재지점에 연결된 노드 꺼내기
            cost  = dist+i[1] # 다음노드까지의 가중치 = 현재까지 가중치 + 현재 ~ 다음 노드까지의 가중치

            if distance[i[0]] > cost: # 다음 노드의 가중치가 계산된 값보다 크면
                distance[i[0]] = cost # 바꾸기(가중치 업데이트)
                heapq.heappush(q,(cost, i[0])) #  다음 가중치와 목적지 큐에 삽입

    return distance

dijkstra(k)

for i in range(1,v+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance(i))