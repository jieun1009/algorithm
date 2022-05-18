import sys
sys.setrecursionlimit(100000) # 원래 파이썬은 1000까지만 recursion함
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*n for _ in range(n)] # n*n만큼 visited 생성

def dfs(x,y,k):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 > nx or nx >= n or 0 > ny or ny >= n: # 범위 초과
            continue 
        else:
            # 방문x and 강수량 k값보다 크면 dfs탐색
            if graph[nx][ny]>k and not visited[nx][ny]:
                visited[nx][ny] =1
                dfs(nx, ny, k)
    
result =0      
# 2차원 배열의 가장 큰 값까지 = 강수량 k
for k in range(max(map(max, graph))):
    visited = [[0]*n for _ in range(n)] # 강수량 바뀔때마다 visited 초기화
    sum = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>k and not visited[i][j]: 
                sum +=1
                dfs(i,j,k) # dfs 다 돌면 sum +1(탐색 돈다= 한개의 안전구역이다)
    result = max(sum, result) # result값 갱신

print(result)



            