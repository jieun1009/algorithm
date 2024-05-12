import heapq

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dijkstra(x,y):
    q = []
    heapq.heappush(q, (x,y, graph[x][y])) # x,y까지의 최단비용 추가
    lose[x][y] = graph[x][y]

    while q:
        x, y, cost = heapq.heappop(q)

        if lose[x][y] < cost: # 더 작으면 갱신할 필요 없음
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if cost+ graph[nx][ny] < lose[nx][ny]:
                lose[nx][ny] = cost + graph[nx][ny]
                heapq.heappush(q, (nx, ny, cost+graph[nx][ny]))
 
cnt = 0
while True:
    cnt+=1
    n = int(input())
    if n ==0:
        break
    INF  = 1e9
    
    graph = [ [0]*(n) for i in range(n)]
    lose = [[INF] * (n) for _ in range(n)]

    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            graph[i][j] = temp[j] 

    
    dijkstra(0,0)
    print(lose)
    print("Problem %d: %d"%(cnt,lose[n-1][n-1]))