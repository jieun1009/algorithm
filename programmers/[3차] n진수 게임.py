def convert(num, n):
    temp = "0123456789ABCDEF"
    q,r = divmod(num, n)

    if q ==0 : # 다 나눠졌으면
        return temp[r]
    else: # 아직 덜 나눠졌으면 q를 다시 나누기
        return convert[q,n] + temp[r] # 몫나머지나머지나머지나머지...

def solution(n, t, m, p):
    answer = ''
    
    num = ''
    for i in range(m*t):
        num += str(convert(i, n))
    
    cnt = 0
    while True:
        cnt+=1
        if t == len(answer):
            return answer
        
        # num 하나씩 제거 
        now = num[0]
        num = num[1:]
        if cnt % m == p % m:
            answer += now # 추가
    
