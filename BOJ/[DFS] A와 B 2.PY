import sys
s = list(input())
t = list(input())

def dfs(string):

    if string == s:
        print(1)
        sys.exit()

    if len(string)<len(s):
        return 0

    # A 떼기
    if string[-1] =="A":
        dfs(string[:-1])
    
    # B 떼기
    if string[0]=="B":
        dfs(list(reversed(string))[:-1])


dfs(t)
print(0) # sys.exit안되면 0 출력
