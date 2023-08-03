def solution(board, moves):
    stack = []

    length = len(board)
    count =0
    for i in moves:
        for j in range(length):
            if board[j][i-1]>0:
                
                if len(stack)>0 and stack[-1] == board[j][i-1]:
                    stack.pop()
                    count +=1
                else:     
                    stack.append(board[j][i-1])
                board[j][i-1] = 0
                break

    
    return count*2