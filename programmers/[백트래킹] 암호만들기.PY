# back tracking version
l,c = map(int, input().split())

arr = sorted(list(input().split()))
vowel = ['a','e','i','o','u']
result = []
answer = []
def back_tracking(cnt, idx):
    if cnt == l : # 단어수가 l만큼 차면
        vowelcnt =0
        consonantcnt = 0

        for i in range(l): 
            if answer[i] in vowel:
                vowelcnt+=1
            else:
                consonantcnt += 1
        
        if vowelcnt>=1 and consonantcnt>=2:
            print(''.join(answer))

    for i in range(idx, c):
        answer.append(arr[i]) # c개의 알파벳을 idx부터 하나씩 answer에 추가
        back_tracking(cnt+1, i+1) # 단어 갯수 추가, 인덱스 추가
        answer.pop() # 해당 단어 빼고 다음 단어 넣기 위함 

back_tracking(0,0)


# combinations version

from itertools import combinations
l,c = map(int, input().split())

arr = list(input().split())
vowel = ['a','e','i','o','u']
result = []

word = list(combinations(arr,l))

for i in range(len(word)):
    vowelcnt =0
    consonantcnt = 0

    for j in word[i]:
        if j in vowel:
            vowelcnt+=1
        else:
            consonantcnt+=1
    
    if vowelcnt>=1 and consonantcnt>=2:
        result.append(list(word[i]))

result = [''.join(sorted(i)) for i in result]

result.sort()

for i in result:
    print(i)