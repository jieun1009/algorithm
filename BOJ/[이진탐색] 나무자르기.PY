n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 0
end = max(tree)



total = 0
while start <= end:
    total = 0
    h = (start+end) // 2

    for i in range(len(tree)):
        if tree[i] > h :
            total += tree[i] - h

            
    if total >= m: # 덜 잘라야 함
        start = h + 1
        print(start,end, "up ",total, h)

    else: # 더 잘라야 함
        end = h - 1
        print(start,end, "down ",total, h)
 
        
print(end)