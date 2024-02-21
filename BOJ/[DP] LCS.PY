str1 = [0] + list(input())
str2 = [0] + list(input())


len1 = len(str1)
len2 = len(str2)
arr = [[0]*len1 for i in range(len2)]


for i in range(1,len2):
    for j in range(1,len1):
        if str1[j] == str2[i]: # 동일할땐 대각선 위 + 1
            arr[i][j] = arr[i-1][j-1]+1
        else: # 다르면 왼쪽, 위쪽 중 긴 것
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])


print(arr[-1][-1])
