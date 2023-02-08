import heapq

n,m,x = map(int, input().split())
arr = [[] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    
INF = 1e9


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in arr[now]:
            cost = dist + i[1]
            
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
           
           
result = [0] *(n+1)     

for i in range(1,n+1):
    distance = [INF]*(n+1)
    dijkstra(i)
    result[i] += distance[x]
    
    distance = [INF]*(n+1)
    dijkstra(x)
    result[i] += distance[i]
    
# print(result)
print(max(result))