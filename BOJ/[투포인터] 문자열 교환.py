arr = list(input())

# b를 하나로 뭉치기
a_cnt = arr.count("a") # a 갯수 = 최종으로 만들어져야 하는 a 문자열 길이 
result = []
n = len(arr)
for i in range(n):

    if i+a_cnt < n:
        cnt = arr[i:i+a_cnt].count("b") # a_cnt만큼 슬라이싱한 문자열에서 b를 다 교환해야 함 
    else:
        cnt = (arr[i:]+arr[:i+a_cnt-n]).count("b") # 이어진 문자열
    result.append(cnt)

print(min(result))
