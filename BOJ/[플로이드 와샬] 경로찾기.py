
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for k in range(n): # 경로가 되는 k의 for문이 가장 상위 단계여야 누락되지 않음!!
    for i in range(n):
        for j in range(n):
            if (graph[i][k]==1 and graph[k][j]==1) or graph[i][j]==1:
                graph[i][j]=1

for i in range(n):
    print(*graph[i])