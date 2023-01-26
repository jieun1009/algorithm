from collections import deque

m,n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

count = 0
# 0을 다 1로 변환될땨까지 +1
bx = [0,1,0,-1]
by = [1,0,-1,0]

q = deque()

first_list= []
for i in range(n):
    for j in range(m):
        if(graph[i][j]==1):
            first_list.append((i,j))
        

def bfs(start):
    for i in range(len(start)):
        q.append(start[i])

    global count
    
    while q:
        count+=1

        for _ in range(len(q)):
            x,y = q.popleft()
            
            for i in range(4):
                nx = x + bx[i]
                ny = y + by[i]

                
                if nx >= n or nx < 0 or ny >= m or ny <0:
                    continue

                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx,ny))


result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            result=1
            break

bfs(first_list)


            
for i in range(n):
    for j in range(m):
        if(graph[i][j]==0):
            result = -1
            break           
            


if result ==1:
    print( count-1)
elif result ==0:
    print("0")
else:
    print("-1")