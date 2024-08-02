MAX =1e9

n = int(input())
arr = list(map(int, input().split()))

building_count = [0]*n # 각 빌딩에서 볼 수 있는 빌딩 숫자
near_building = [MAX]*n # 볼 수 있는 건줄 중 가장 가까운 빌딩

# 왼쪽에서 오른쪽 탐색

left_stack = []
for i, height in enumerate(arr):
    
    while left_stack and arr[left_stack[-1]] <= height: # 마지막 스택의 값 비교
        left_stack.pop() # 나보다 작으면 다 빼기
        
    building_count[i] += len(left_stack)
    
    if left_stack:
        if abs(near_building[i]-i) > abs(i - left_stack[-1]): # right와 비교하기 위함
            near_building[i] = left_stack[-1]
        
    left_stack.append(i)
    
# 오른쪽에서 왼쪽 탐색

right_stack = []
for i in range(n-1, -1,-1):
    height = arr[i]
    
    while right_stack and arr[right_stack[-1]] <= height:
        right_stack.pop()
        
    building_count[i] += len(right_stack)
    
    if right_stack:
        if abs(near_building[i]-i) > abs(i - right_stack[-1]):
            near_building[i] = right_stack[-1]
        
    right_stack.append(i)
    
    
for i in range(n):    
    if building_count[i]:
        print(building_count[i], near_building[i]+1)
    else:
        print(0)