n, m = map(int, input().split())
friends = [[1000]*(n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    friends[a][b]=1
    friends[b][a]=1

min_value = n*6

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                friends[i][j]=0 # 자기자신
            else:
                friends[i][j] = min(friends[i][j], friends[i][k]+ friends[k][j])
person = []
for i in friends:
    person.append(sum(i))

print(person.index(min(person)))