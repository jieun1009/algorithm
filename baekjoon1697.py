import collections

# 입력
n,k = map(int, input().split())
move = []
max = 100000
visited = [0]*(max+1) # 이동 가능한 최대 방향만큼 리스트 생성

def bfs(n):
    q = collections.deque()
    q.append(n) 
    
    while q:
        v=q.popleft()
        if v == k: # while문 돌며 k값에 도달하면 중지
            print(visited[v])
            break

        
        for i in (v-1,v+1,2*v):
            if 0<=i<=max and not visited[i]: # visited[i]==0(방문x) 이고 i가 최대 범위를 넘지 않을때
                q.append(i)
                visited[i]=visited[v]+1
                
        # move = [v-1,v+1,2*v]
        # # x-1/x+1/2*x 를 큐에 추가
        # if 0<= v <=max and not visited[v]: 
        #     # 이 코드로 하면 안되는 이유: v로 조건을 돌림(v-1/v+1/2*v로 돌려야 함)
        #     q.append(move[0])
        #     q.append(move[1])
        #     q.append(move[2])
        #     visited[move[0]]=(visited[v]+1)
        #     visited[move[1]]=(visited[v]+1)
        #     visited[move[2]]=(visited[v]+1)
                

        
        
bfs(n)