n = int(input())
arr = [0]

for _ in range(n):
    arr.append(int(input()))

first = set()
second = set()
result=set()

def dfs(f_idx, first, second):
    if arr[f_idx] not in second:
        first.add(f_idx)
        second.add(arr[f_idx])
        if first == second: # 사이클 발생
            result.update(first) # 현재까지 숫자 결과에 반영
            return 
        else:
            # 기존의 값들 더 탐색
            dfs(arr[f_idx], first, second) 



for i in range(1,n+1):
    if i not in first: # 새로운 set으로 탐색
        dfs(i,set(), set())

print(len(result))
print(*sorted(list(result)), sep="\n")