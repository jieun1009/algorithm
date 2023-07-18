def solution(cards1, cards2, goal):
    
    answer = 'No'
    gindex = len(goal)
    index1 = 0
    index2 = 0
    
    for i in range(len(cards1)+len(cards2)+1):
        if len(goal) == 0:
            answer = 'Yes'
        
        if gindex > i:
            if index1 < len(cards1) and goal[0] == cards1[index1]:
                goal.pop(0)
                index1 +=1
            elif index2 < len(cards2) and goal[0] == cards2[index2]:
                goal.pop(0)
                index2 += 1
            
    return answer