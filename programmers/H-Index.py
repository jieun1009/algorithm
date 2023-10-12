def solution(citations):
    
    n = len(citations)
    citations.sort()

    for i in range(n):
        if citations[i] >= n-i:
            return n-i # 인용 횟수가 인덱스보다 커지는 순간 리턴
    return 0