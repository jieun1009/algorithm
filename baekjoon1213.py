name = input()
name = list(name)
name.sort()

length = len(name)
start = 0
end = len(name)-1
count= 0
tmp = "null"
for i in set(name):
    if name.count(i) %2 ==1: # 홀수개있을때
        count+=1
        if count>1 :
            print("I'm Sorry Hansoo")
            exit(0)
        odd_index = name.index(i)
        tmp = name[odd_index]
        name.remove(tmp)

index = 0
result=[0]*length

for i in range(0,length-1,2):
    start = index
    result[start]=name[i]
    index+=1
    end = length - start -1
    result[end]=name[i+1]
        
if tmp!="null":
    start = len(name)//2
    result[start]=tmp
# print(name)
 
print("".join(result))