n,m,l,k = map(int, input().split())
arr = list()

for _ in range(k):
    a,b = map(int,input().split())
    arr.append((a,b))
    
MAX = 0
cnt = 0
for i in range(len(arr)): # 첫번째 별
    for j in range(len(arr)): # 두번째 별
        cnt = 0
        
        # 두 별을 걸치는 가장 왼쪽 상단 좌표(두 별 중 더 왼쪽 위의 좌표)
        sx, sy = min(arr[i][0],arr[j][0]), min(arr[i][1],arr[j][1])    
        
        for x, y in arr:
            if sx <= x <=sx+l and sy <= y <= sy+l:
                # x,y(별)이 트램펄린 안에 속함
                cnt+=1
                    
        MAX = max(MAX, cnt)        
        
print(k-MAX) # 지구에 부딪히는 별똥별 개수