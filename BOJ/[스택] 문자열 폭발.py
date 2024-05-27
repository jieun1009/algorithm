import sys
string = list(input())
bomb = list(input())
bomblen = len(bomb)

stack = []


for i in string:
    stack.append(i)

    if stack[len(stack) - len(bomb): len(stack)] == bomb:
        
        for _ in range(len(bomb)):
            stack.pop()
    
print(''.join(stack) if stack else "FRULA")