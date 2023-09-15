def solution(n):
    # k 만큼 점프 = k만큼 감소, 지금 거리*2 순간이동
    ans = 0

    # n을 2로 나눠가며 홀수가 나올때마다 점프!
    while(n!=1):
        if(n%2==1) : # 홀수면 점프
            ans+=1
            n-=1
        n = n//2
    
    
    # n이 1 : 맨 처음 점프 무조건 필요함
    ans+=1
    
    
    return ans