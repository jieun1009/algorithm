n = int(input())
arr = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())

max_value = -1e9
min_value = 1e9

def dfs(index, result):
    global add, sub, mul, div, max_value, min_value
    if index == n : # 주어진 수열 끝까지 계산 완료
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    else:
        if add > 0: # 더하기 수행 후 dfs 진행(다음 계산 진행) 후 다시 취소
            add -=1 
            dfs(index+1, result + arr[index])
            add+=1
        if sub >0:
            sub -=1
            dfs(index+1, result-arr[index])
            sub+=1
        if mul >0:
            mul -=1
            dfs(index+1, result*arr[index])
            mul+=1
        if div>0:
            div-=1
            dfs(index+1, int(result/arr[index]))
            div+=1

dfs(1,arr[0])

print(max_value)
print(min_value)