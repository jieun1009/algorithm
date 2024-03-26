t = int(input())

for _ in range(t):
    w = list(input())
    k = int(input())

    alpha = dict()

    if k==1:
        print(1,1)
        continue

    for i, char in enumerate(w):
        if char not in alpha:
            alpha[char] = [i]
        else:
            alpha[char].append(i)

    short = 10e9
    long =0
    for x in alpha.values():
        if len(x) >=k:
            for i in range(len(x)-k+1): # k개chunk로 돌아가기 위해 마지막 값을 k개 전으로!
                # 가장 짧기 위해서도 동일한 문자열이 앞, 뒤에 있어야 하므로 가장 긴 문자열(+앞,뒤 같은 문자) 조건은 동일하게 사용
                if short > x[i+k-1] - x[i]+1: # k개 chunk
                    short = x[i+k-1] - x[i]+1 
                if long < x[i+k-1] - x[i]+1: # k개 chunk
                    long = x[i+k-1] - x[i]+1


    if short ==10e9 or long==0:
        print(-1)
        continue
    print(short, long)

