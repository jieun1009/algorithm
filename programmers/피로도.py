answer = 0
def solution(k, dungeons):
    global answer  
    visited = [0]*len(dungeons)
    def dfs(k, dungeons, visited, cnt):
        global answer
        answer = max(answer, cnt)
        for idx, i in enumerate(dungeons):
            if visited[idx]==0 and k >= i[0]:
                visited[idx] =1
                dfs(k-i[1], dungeons, visited, cnt+1)
                visited[idx]=0
                
    dfs(k, dungeons, visited, 0)
    
    return answer