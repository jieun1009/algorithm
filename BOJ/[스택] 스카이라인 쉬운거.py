n=int(input())

# 들어오는 숫자가 높아지면 새로운 층이 시작한다는 것
# 들어오는 숫자가 낮아지면 해당 층이 끝났다는 것
stack = [0]
cnt = 0
for _ in range(n):
    w, h = map(int, input().split())
    if stack[-1] < h : # 새로운 층 시작
        cnt+=1
        stack.append(h)
    else: # 새로운 층 끝남
        while stack[-1] > h: 
            stack.pop() # 현재 h가 스택에서 가장 큰 값이 될때까지 pop
        if h not in stack and h!=0:
            stack.append(h)
            cnt+=1
print(cnt)