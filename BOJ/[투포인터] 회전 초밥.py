n,d,k,c = map(int, input().split()) # 접시수, 초밥 가짓수, 연속 접시수, 쿠폰 번호

sushi = []
for _ in range(n):
    sushi.append(int(input()))

start = 0
end = k-1
cnt = 0
while start < n:
    if end >= n: # 회전이므로!
        end -= n
    if end < start:
        plate = sushi[start:] + sushi[:end+1]
    else:
        plate = sushi[start:end+1] 

    temp = set(plate)
    if c not in temp:
        temp.add(c) # 쿠폰 초밥 추가
    cnt = max(cnt, len(temp))

    start+=1
    end+=1

print(cnt)
