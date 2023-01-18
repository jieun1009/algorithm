n = int(input())
street = list(map(int, input().split()))
oil = list(map(int,input().split()))

result =0 


min_oil=oil[0]
idx = 0
for i in oil:
    if i < min_oil:
        min_oil=i
    result += (min_oil*street[idx])
    idx+=1
    if idx == len(street):
        break
    
print(result)