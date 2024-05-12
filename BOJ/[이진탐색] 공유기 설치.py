n,c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

# 공유기 사이 거리를 이진탐색해서 최대 값 찾기
start = 1 # 최솟값
end = arr[-1] - arr[0] # 최댓값
result = 0 

while start <= end: 
    mid = (start + end) // 2 # 공유기 사이 거리
    current = arr[0] # 공유기 설치 위치
    count = 1 # 공유기 설치 갯수

    for i in range(1, len(arr)): # 거리 맞춰 공유기 설치
        if mid <= arr[i] - current:
            count +=1
            current = arr[i]

    if count >= c: # 더 많이 설치할 수 있으면 거리 늘림
        start = mid +1
        result = mid
    else:
        end = mid-1 # 좌표가 아닌 거리니까 mid-1 가능
    
print(result)