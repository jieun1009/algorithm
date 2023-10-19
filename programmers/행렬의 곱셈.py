def solution(arr1, arr2):
    
    answer = []

    for i in range(len(arr1)):
        arr = [0]*len(arr2[0])
        for j in range(len(arr1[i])):
            for k in range(len(arr2[0])):
                temp = arr1[i][j] * arr2[j][k]
                arr[k] += temp 
        answer.append(arr)
                
    
    
    return answer