def solution(files):
    answer = []

    head, number, tail = '','',''
    filearr = []
    # 문자열 처리
    for i in range(len(files)):
        file = files[i]

        num = 0 # number 시작되는 index
        for f in range(len(file)):
            if file[f].isdigit():
                head = file[:f]
                number = file[f:]
                break

        for f in range(len(number)): # number부터 tail 추출
            if number[f].isdigit()==False or f>=5: # 숫자가 아니거나 다섯자리를 넘어서면 tail
                tail = number[f:]
                number = number[:f]
                break
        filearr.append((head,number,tail))
        head, number, tail = '','',''
  
    filearr = sorted(filearr, key = lambda file: (file[0].lower(), int(file[1])))
    for i in filearr:
        answer.append(''.join(i))
    return answer