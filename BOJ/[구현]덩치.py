n = int(input())

arr = []
result = [1]*n
for _ in range(n):
    arr.append(list(map(int,input().split())))

# arr.sort()
# for i in range(arr):
#     for j in range(i+1, arr):
#         if arr[i][1] <= arr[j][1]:
#             result[i]+=1

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1] and i!=j:
            result[i]+=1


for i in result:
    print(i, end=' ')