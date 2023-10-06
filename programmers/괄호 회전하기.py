def solution(s):
    answer = 0

    for i in range(len(s)):
        # 한바퀴 왼쪽으로 
        if i!=0:
            temp= s[i:]+s[:i]
        else:
            temp = s

        for j in range(len(temp)):
            temp = temp.replace("()","")
            temp = temp.replace("{}","")
            temp = temp.replace("[]","")


        if len(temp)==0:
            answer+=1
        

    return answer