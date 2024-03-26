from collections import deque

n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0 for i in range(n)]

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]: # 큰 건물 발견
            answer[i] = stack[-1][0] + 1
            break
        else: # 현재 탑이 더 큰 경우, 어차피 현재가 더 높으니 작은것은 필요없음
            stack.pop()

    if not stack:
        answer[i] = 0

    stack.append([i,top[i]]) # 탑의 인덱스와 높이는 일단 stack에 집어 ㄴ허기

print(*answer)