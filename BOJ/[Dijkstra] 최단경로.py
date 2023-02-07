import sys
import heapq

v,e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
arr = [[] for i in range(v+1)]
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    
INF = 1e9
distance = [INF] *(v+1)
distance[start] = 0
def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for i in arr[now]:
            cost = dist + i[1]
            
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else : print(distance[i])