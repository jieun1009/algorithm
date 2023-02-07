import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    
start , end = map(int,sys.stdin.readline().split())

INF = 1e9
distance = [INF]*(n+1)
distance[0] = 0
def dijkstra(x):
    q = []
    heapq.heappush(q, (0,x)) # dist, now 
    distance[x] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
    
                
    return distance



dijkstra(start)
print(distance[end])