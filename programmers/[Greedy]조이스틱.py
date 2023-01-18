def solution(name):
    answer = 0
    
    # 어차피 j로 이동하려면 a에서 9번 조작 = 총 이동 후 -65 하면 됨
    for i in range(len(name)):
        min_value_A = (ord(name[i])-ord("A"))
        min_value_Z = (ord("Z")-ord(name[i]))+1
        
        answer += min(min_value_A,min_value_Z)

    front = 0
    for i in range(len(name)-1):
        if name[i+1]=="A":
            break
        front+=1
        
    back=0
    for i in range(len(name)-1,0,-1):
        if name[i-1]=="A":
            break
        back+=1
    
    A=0
    for i in range(len(name)-1):
        if name[i]=="A" and name[i+1]=="A":
            A+=1
    # 오른쪽으로 갔다가 왼쪽으로 가는 경우     
 
    result_right =front*2 +1+back
        
    
    
    # 처음부터 왼쪽으로 갔다가 오른쪽 가는 경우
    result_left =1+(back*2)+1+front


    
    answer+=min(len(name)-1,result_left,result_right)

    return answer

print(solution("ABAAAAABAB"))