from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    bx = [1,0,-1,0]
    by = [0,1,0,-1]
    
    def bfs(x,y): 
        queue = deque()
        queue.append([x,y])

        while(queue):
            x,y = queue.popleft()
            for i in range(4):
                nx = x+bx[i]
                ny = y+by[i]

                if(0<=nx<n and 0<=ny<m):
                    if(maps[nx][ny]==1):
                        # 범위내에 있고 다음 좌표가 벽이 아니면 큐에 추가
                        maps[nx][ny] = maps[x][y] +1
                        queue.append([nx,ny]) 
        return maps[n-1][m-1]
        
    answer = bfs(0,0)
    
    # 벽에 막혀 최종 방문 불가
    if maps[n-1][m-1]==1:
        return -1
    
    
    return answer