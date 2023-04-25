n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
visited = [False for i in range(n)]

min_value = int(1e9)

def dfs(depth, index):
    global min_value
    # 절반까지 돌면(스타트팀 배정 완료)
    if depth == n//2:
        start, link  = 0,0
        for i in range(n):
            for j in range(n):    
                if visited[i] and visited[j]: # i선수와 j선수가 visited에 들어감 = 스타트팀
                    start += arr[i][j]
                elif not visited[i] and not visited[j]: # i선수와 j선수가 visited에 안들어감 = 링크팀
                    link += arr[i][j] 
        min_value = min(min_value, abs(start - link))
        return
        
    for i in range(index, n): # 팀 배정 아직 안됐으면 현재 인덱스부터 수행
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i]= False
            
    
dfs(0,0)
print(min_value)




result = []
def dfs(start, result):
    if len(result) == 6:
        print(*result)
        return
    
    for i in range(start,k+1):
    
        if len(result)==0:
            result.append(arr[i])
            dfs(i+1, result)
            result.pop()
        else: 
            # arr엔 숫자가 순서대로 들어있으니 result[-1]보다 크면
            # result에 더 들어갈 수 있는 상태!
            if arr[i] > result[-1]:
                result.append(arr[i])
                dfs(i+1, result)
                result.pop()
        

while(True):
    arr = list(map(int, input().split()))
    k = arr[0]
    if k ==0:
        break
    dfs(1,result)
    print()
