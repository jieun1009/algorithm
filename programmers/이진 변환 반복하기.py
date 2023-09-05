def solution(s):
    
    zero_cnt = 0
    count = 0
    while(s!='1'):
        count +=1
        if "0" in s:
            zero_cnt += s.count("0") # 제거할 0 개수
            s= s.replace("0","") 
        # s의 길이를 이진수로 변환
        length = len(s)
        s= str(format(length,'b')) #2진수로 변환
        
        
    answer = [count , zero_cnt]
    return answer