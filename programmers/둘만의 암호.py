def solution(s, skip, index):
    answer = ''
    arr = []
    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in skip:
            arr.append(i)       

    for i in s:
        idx = arr.index(ord(i))
        if idx + index < len(arr):
            answer += chr(arr[idx+index])
        else:
            answer += chr(arr[(idx+index) % len(arr)])

    return answer