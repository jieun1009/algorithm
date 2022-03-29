n= int(input())
loop=[]
for _ in range(n):
    a=int(input())
    loop.append(a)
    
loop.sort()
w=loop[0]*n

for i in range(n):
    next_w=loop[i]*(n)
    # print("next= ",next_w)
    if(w<=next_w):
        w=next_w
    n-=1
    i+=1

print(w)
