t = int(input())
resultlist = []
def back_tracking(i, n,string):
    if i==n-1: # 계산
        num = []
        oper = []
        for s in range(len(string)):
            if string[s] == "+" or string[s]=="-":
                oper.append(string[s])
            elif string[s]==" ":
                num[-1]= num[-1]*10 + int(string[s+1])
                
            elif s==0 or string[s-1]!=" ":
                num.append(int(string[s]))
        temp = num[0]
        if len(oper)+1 == len(num):
            for n in range(1,len(num)):
                if oper[n-1] == "+":
                    temp += num[n]
                else :
                    temp -= num[n]
            if temp ==0:
                resultlist.append(string)


    else:
        # 더하기
        back_tracking(i+1, n, string+'+'+str(arr[i+1]))
        # 빼기
        back_tracking(i+1, n, string+'-'+str(arr[i+1]))
        # 공백 삽입
        back_tracking(i+1, n, string+' '+str(arr[i+1]))

for _ in range(t):
    resultlist = []
    n = int(input())

    arr = []
    for i in range(1, n+1):
        arr.append(i)

    back_tracking(0, n, str(arr[0]))
    
    resultlist.sort()
    for i in range(len(resultlist)):
        print(resultlist[i])
    print()
    

