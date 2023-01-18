import heapq

n = int(input())
arr =[]

for _ in range(n):
    heapq.heappush(arr, int(input()))


result = 0
if n ==1:
    print(0)
else:
    while len(arr)>1: # 큐에 카드가 다 빠질때까지
        sum_value = heapq.heappop(arr) + heapq.heappop(arr)
        result += sum_value
        heapq.heappush(arr, sum_value)
        
        


    print(result)