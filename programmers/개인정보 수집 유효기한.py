def solution(today, terms, privacies):
    
    arr = today.split(".")
    year = int(arr[0])
    month = int(arr[1])
    day = int(arr[2])
    answer = []
    deadline = {}
    for i in terms:
        deadline[i.split()[0]] = int(i.split()[1])
    
    for idx,i in enumerate(privacies):
        date = i.split()[0]
        to_year = int(date.split(".")[0])
        to_month = int(date.split(".")[1])
        to_day= int(date.split(".")[2])
        dead = i.split()[1]

         # 만료일
        y=to_year
        m=to_month+deadline[dead]
        d=to_day -1
        
        if (to_month + deadline[dead] > 12):
            y += (to_month+ deadline[dead])//12
            m = (to_month  + deadline[dead]) % 12
            
            if m ==0:
                m=12
                y-=1

        # 기한 넘김 1. 년도가 오늘보다 전 2. month가 오늘보다 전 3. 
        # 년도가 어차피 today보다 뒤
        if(y<year):
            answer.append(idx+1)
            
        elif(y==year and m < month):
            answer.append(idx+1)
            
        elif(y==year and m==month and d<day):
            answer.append(idx+1)

    return answer