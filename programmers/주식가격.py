def solution(prices):

    stack = []
    for i in range(len(prices)):
        stack.append(0)
        for j in range(i+1, len(prices)):
            stack[i]+=1
            if prices[i] > prices[j]:
                break
    
    return stack