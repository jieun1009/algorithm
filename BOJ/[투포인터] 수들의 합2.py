import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

count = 0 
interval_sum = 0 # 현재 부분 수열의 합
start = 0
end = 1

while start <= end and end <= n:

    temp_arr = arr[start:end]
    interval_sum = sum(temp_arr)
    if interval_sum > m: # 더 크면 start 증가
        start += 1
    
    if interval_sum == m: # 부분합이 m일때 카운트 증가, 그 다음 값으로 이동
        count +=1
        start += 1
        
    if interval_sum < m: # 더 작으면 end 증가
        end+=1
        
     

    
print(count)