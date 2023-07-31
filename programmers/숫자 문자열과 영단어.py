def solution(s):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = 0

    for i in range(len(num)):
        if num[i] in s:
            s = s.replace(num[i],str(i))
    answer = int(s)
    return answer