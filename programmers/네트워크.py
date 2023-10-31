def dfs(x,y,computers):
    computers[x][y]=0 #방문처리
    computers[y][x]=0
    n= len(computers)
    
    for i in range(n):
        if computers[x][i] == 1:
            # 같은 행에 또 연결된 네트워크 있다면 dfs
            dfs(i,x,computers)
    

def solution(n, computers):
    answer = 0
    n = len(computers)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1: # 연결됨
                dfs(j,i,computers)
                answer+=1
    
    return answer