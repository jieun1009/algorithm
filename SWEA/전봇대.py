T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # 총 전선 수
    line = []
    for _ in range(n):
        a, b = map(int,input().split())
        line.append([a,b])
        
    line.sort() # 가장 낮은곳에 있는 전선을 맨 앞에!
    cnt = 0
    for i in range(1, n): # 두번째 전선부터 비교
        for j in range(0, i):
            # 왼쪽엔 나보다 낮게 있는 전선이 오른쪽엔 나보다 높은지 확인
            if line[i][1] <= line[j][1]:
                cnt+=1
    print("#{} {}".format(test_case, cnt))
    
    # 풀이 방법
    # 왼쪽 전봇대에 나보다 아래에 있고, 동시에 오른쪽 전봇대에 나보다 위에 있으면 교차