wordlist = []
ans = 0
dic = {}

n = int(input())
for _ in range(n):
    wordlist.append(input())

# 1번 수행
for i in wordlist:
    cnt = len(i)
    for j in i:
        if j not in dic:
            dic[j] = 10**(cnt-1)
        else:
            dic[j]+=(10**(cnt-1))
        cnt-=1

# 2번 수행
valuelist = list(dic.values())
valuelist.sort(reverse=True)

# 3번 수행
num = 9
for i in valuelist:
    ans+= i*num
    num-=1

print(ans)