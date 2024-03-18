import heapq

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
INF = 1e9


for i in range(d):
    graph[i].append((i+1, 1)) # i+1 목적지의 가중치는 1로 초기화

# 지름길 추가
for i in range(n):
    a,b,c = map(int, input().split())
    if b>d: continue # b가 최종 목적지보다 크면 패스
    graph[a].append((b, c)) 
    
distance = [INF]*(d+1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # start까지의 가중치는 0

    while q:
        dist, now = heapq.heappop(q) # 가장 거리가 짧은 노드 pop/ dist=목적지까지의 가중치, now: 현재 꺼내진 노드

        if dist > distance[now]:
            continue # now까지의 가중치가 작아야 다음 실행 


        # 다음 목적지 가중치 업데이트 
        for node in graph[now]: # 현재 node와 연결된 node 꺼내기
            # node[0] 목적지
            # node[1] 가중치
            cost = dist+ node[1] # 현재까지의 가중치 + 다음 node까지의 가중치
            if cost < distance[node[0]]:
                distance[node[0]]= cost
                heapq.heappush(q,(cost, node[0]))

dijkstra(0)
print(distance[d])