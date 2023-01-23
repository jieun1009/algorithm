n = int(input())
arr = []
for i in range(6):
    arr.append(list(map(int,input().split())))

# 긴*긴
w = 0; widx = 0
h = 0; hidx = 0
for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] ==2:
        if w <=arr[i][1]:
            w = arr[i][1]
            widx = i
            
    if arr[i][0] == 3 or arr[i][0] ==4:
        if h <=arr[i][1]:
            h = arr[i][1]
            hidx = i



# 짧*짧
small_w, small_h = 0,0
idx_w = 0
idx_h = 0

small_w = abs(arr[(widx-1)%6][1] - arr[(widx+1)%6][1])
small_h = abs(arr[(hidx-1)%6][1] - arr[(hidx+1)%6][1])       


print((hidx-1)%6)
print((w*h - small_h*small_w)*n)


        
