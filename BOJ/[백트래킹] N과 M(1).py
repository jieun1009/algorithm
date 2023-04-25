n,m = map(int, input().split())

arr = []
result = []
def dfs():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1): # 1~n 
        if i not in arr: # 아직 수열에 안들어갔으면
            arr.append(i) # 수열에 추가
            dfs() # dfs 돌려서 i 다음 값 확인 + m만큼뽑으면 출력
            arr.pop() # i 빼기
            # [1] -> [1,2] -> pop [1] -> [1,3] -> pop[1]
            
dfs()