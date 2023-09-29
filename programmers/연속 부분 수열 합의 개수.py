def solution(elements):
    answer = 0
    result = set()
    length = len(elements)
    for i in range(0, length):
        arr = []
        for j in range(0,len(elements)+1):
            if (j+i<length):
                temp = sum(elements[j:i+j])  
            else: 
                temp = sum(elements[j:]+ elements[:i-length+j])
            result.add(temp)

    return len(result)