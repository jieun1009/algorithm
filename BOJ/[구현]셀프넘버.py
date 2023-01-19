
checked = [False]*10001
# 최대 9999까지 확인(총 4자리)
for i in range(1,10000):
    idx = i + sum(map(int, str(i)))
    if idx <= 10000:
        checked[idx] = True
       
    
for i in range(1,10001):
    if checked[i]==False:
        print(i)

