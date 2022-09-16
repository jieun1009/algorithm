n,m=map(int,input().split())
arr =[]
def dfs():
    if len(arr) == m:
        print(' '.join(map(str,arr))) # n개 다 고르면 프린트
        return
    for i in range(1,n+1):
        if i not in arr and ( len(arr)==0 or arr[-1]< i ): #오름차순/ 비어있으면 그냥 채움
            arr.append(i) # arr에 없으면 넣고 
            dfs() # dfs 돌려서 m개 채움
            arr.pop() # i 빼고 다음 돌림
            
            
dfs()
     