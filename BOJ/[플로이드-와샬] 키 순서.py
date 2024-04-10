n, m = map(int, input().split())

arr = [[0]*(n) for _ in range(n)] # n*n 배열
answer = 0
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1]=1 # a,b는 키 비교 가능
    

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k]==1 and arr[k][j]==1: # i>k 이고 k>j 이면 i>j 가능
                arr[i][j]=1
                
                
for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[i][j] + arr[j][i] # j보다 작은 사람 + j보다 큰사람의 합
        
    if sum == n-1:
        answer+=1

print(answer)