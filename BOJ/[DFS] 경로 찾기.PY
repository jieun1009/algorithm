n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))


# # 하나의 노드에 도달할때까지 깊이 파고들어야 하므로 dfs
def dfs(x):
    for i in range(n):
        if graph[x][i]==1 and check[i]==0: # 방문 안했고, 해당 행에 간선이 있다면
            check[i]=1 # x 행의 i 1로 만들기 (방문 리스트이자 연결그래프)
            dfs(i) # 그 행으로 이동


for i in range(n):
    check = [0 for _ in range(n)]
    dfs(i)
    print(*check)