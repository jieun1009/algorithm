import heapq

n, m = map(int, input().split())

arr = [[] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))
    
INF = 1e9
distance = [INF]*(n+1)

def dijkstra(start):
    q =[]
    heapq.heappush(q,(0,start))
    
    while q:
        meal, now = heapq.heappop(q)
        
        if distance[now] < meal:
            continue
        
        for i in arr[now]:
            total = meal + i[1]
           
            if total < distance[i[0]]:
                distance[i[0]] = total
                heapq.heappush(q, (total, i[0]))
                
dijkstra(1)
print(distance[n])