str1 = [0] + list(input())
str2 = [0] + list(input())


len1 = len(str1)
len2 = len(str2)
dp = [[0]*len1 for i in range(len2)]


for i in range(1,len2):
    for j in range(1,len1):
        if str1[j] == str2[i]: # 동일할땐 대각선 위 + 1
            dp[i][j] = dp[i-1][j-1]+1
        else: # 다르면 왼쪽, 위쪽 중 긴 것
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
if dp[-1][-1]!=0:
    answer = ''

    # 두 문자열의 길이를 얻은 값이서 출발 (위에서 돌은 for의 마지막)
    i = len2-1
    j = len1-1

    while i> 0 and j> 0:
        if dp[i][j-1] == dp[i][j]:
            j-=1 # 왼쪽으로 이동
        elif dp[i-1][j] == dp[i][j]:
            i-=1 # 위쪽으로 이동
        else:
            # 두 수가 동일하면, 앞에 붙이고
            # 대각선으로 이동
            answer =str1[j] + answer
            i-=1
            j-=1 

    print(answer)
