n= int(input())
bulbs = list(map(bool, map(int, input())))
answer = list(map(bool, map(int, input())))

def push(arr, i, flag, cnt):
    
    if flag==True:
        cnt +=1

        # i-1 push
        if not arr[i-1] and i!=0:
            arr[i-1] = True
        elif arr[i-1] and i!=0:
            arr[i-1]= False
        # i push 
        if not arr[i]:
            arr[i] = True
        else:
            arr[i]= False
        # i+1 push 
        if i!=n-1 and not arr[i+1] :
            arr[i+1] = True
        elif i!=n-1 and arr[i+1]:
            arr[i+1]= False

    return arr, cnt

on = bulbs.copy()
off = bulbs.copy()

for i in range(len(bulbs)):

    if i ==0:
        # push 함
        bulbs_on, cnt_on = push(on, i, True, 0)

        # push 안함
        bulbs_off, cnt_off = push(off, i, False, 0)

    else:
        
        # 1부터는 이전값이 정답과 다르면 push 
        if bulbs_on[i-1]!=answer[i-1]:
            bulbs_on, cnt_on = push(bulbs_on,i,True, cnt_on)
        if bulbs_off[i-1]!=answer[i-1]:
            bulbs_off, cnt_off = push(bulbs_off,i,True, cnt_off)

result = float("INF")
if bulbs_on==answer:
    result = min(result, cnt_on)
if bulbs_off==answer:
    result=min(result, cnt_off)


if result==float("INF"):
    print(-1)
else:
    print(result)