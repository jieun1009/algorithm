## 내가 푼 코드

# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
    
# stack_arr = []
# result = []
# max_value = 0


# # 초기화 작업 - 맨 처음 수만큼 스택에 넣는 작업
# for k in range(1,arr[0]+1):
#     stack_arr.append(k)
#     result.append("+")


# for i in range(n):

#     # 스택에 값이 없는 경우 실행 x
#     if len(stack_arr)!=0:
#         max_value = max(max_value, max(stack_arr))

#     # 이미 스택에 들어간 숫자 더 넣지 않게 하기 위해
#     if max_value == arr[-1]:
#         for i in range(len(stack_arr)):
#             stack_arr.pop()
#             result.append("-")
#             break
 
    
#     if len(stack_arr)>0:
#         # 스택 top과 arr 현재 값 비교해 동일하면 pop

#         if stack_arr[-1] == arr[i]:
#             result.append("-")
#             stack_arr.pop()
            
#         # 스택 top과 arr 현재 값 비교해 arr 현재값이 더 크면 push
#         elif stack_arr[-1] < arr[i]:
         
#             for k in range(max_value+1,arr[i]+1):
#                 stack_arr.append(k)
#                 result.append("+")

         
#             max_value = max(max_value, max(stack_arr))
            
#             result.append("-")
#             stack_arr.pop()
            
            
    
    
#     # 더 작은 경우는 어차피 no라서 안함
        

        
# if len(result) != (n*2):
#     print("NO")
# else:
#     for i in range(len(result)):
#         print(result[i])           
        
        
## 답안

n = int(input())
stack_arr=[]
result = []
count =1
for i in range(n):
    # 초기화 작업
    num = int(input())
    while count <= num:
        stack_arr.append(count)
        result.append("+")
        count +=1
    
    if stack_arr[-1] == num:
        stack_arr.pop()
        result.append("-")
    
    
if len(result) != (n*2):
    print("NO")
else:
    for i in range(len(result)):
        print(result[i])
