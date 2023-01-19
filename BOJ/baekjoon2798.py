import itertools

n,m=map(int,input().split())
numArr=list(map(int,input().split()))

combination = list(itertools.combinations(numArr,3))
result=list()
for i in range(len(combination)) :
    com=combination[i][0]+combination[i][1]+combination[i][2]
    if(m>=com):
        result.append(com)
    

min=result[0]
for i in range(len(result)):
        if(m-min>=(m-result[i])):
            min=result[i]

print(min)