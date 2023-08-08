def solution(numbers, hand):
    # 1,4,7 : 왼손
    # 3,6,9 : 오른손
    # 2,5,8,0 : 가까운손 (거리 동일시 오른손잡이=R, 왼손잡이=L)
    result = []
    left = -1
    right = -1
    arr = [[1,3,5],[4,6,8],[7,9,0],[-1],
           [2,4,6,8],[1,3,7,9,0],[-1],
           [5,7,9,0],[2,4,6,-1],[1,3],
           [8,-1],[5,7,9],[2,4,6],[1,3]]
    for i in numbers:

        leftcnt = 0
        rightcnt = 0
        if i == 1 or i==4 or i ==7:
            result.append('L')
            left = i
        elif i==3 or i==6or i==9:
            result.append('R')
            right = i
        else:
            
            if i==2:
                for j in range(0,4):
                    if left in arr[j]:
                        leftcnt += (j+1)
                    if right in arr[j]:
                        rightcnt += (j+1)
            elif i==5:
                for j in range(4,7):
                    if left in arr[j]:
                        leftcnt += (j-4+1)

                    if right in arr[j]:
                        rightcnt += (j-4+1)

            elif i==8:
                for j in range(7,10):
                    if left in arr[j]:
                        leftcnt += (j-7+1)
                    if right in arr[j]:
                        rightcnt += (j-7+1)

            elif i==0:
                for j in range(10,14):
                    if left in arr[j]:
                        leftcnt += (j-10+1)
                    if right in arr[j]:
                        rightcnt += (j-10+1)

            
            if i== left or i ==right:
                if left==i:
                    leftcnt=0
                elif right ==i:
                    rifhtcnt =0

                    
            if leftcnt < rightcnt:
                result.append('L')
                left = i
            elif leftcnt > rightcnt:
                result.append('R')
                right = i
            else:
                if hand == "right":
                    result.append('R')
                    right = i
                else:
                    result.append('L')
                    left = i
    pnt = ''.join(result)

    return pnt