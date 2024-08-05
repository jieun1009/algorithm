n,a,b = map(int, input().split())

building = list(i+1 for i in range(a))

if b != 1:
    if b>a:
        building[-1] = b

    for i in range(b-1,0,-1):
        building.append(i)
            
if len(building) > n:
    print(-1)
    exit(0)
elif len(building) < n:
    for _ in range(n-len(building)):
        building.insert(1,1)
        
print(*building)
