from collections import deque

def solution(begin, target, words):
    answer = 0 
    if target not in words:
        return 0
    
    if begin in words: # 이미 words에 있다면 제거
        words.remove(begin)
    
    q = deque()
    q.append((begin,0))
    
    word = begin
    cnt = 0
    while(q):
        word, cnt = q.popleft()  
        
        if(word == target):
            break

        for i in range(len(begin)):
            b_word = word[0:i]+word[i+1:]
            list_word = [ x[0:i]+x[i+1:] for x in words]
            
            if b_word in list_word:
                index = list_word.index(b_word)
                temp = words[index] # 원래 단어로 복구
                q.append((temp, cnt+1)) # 큐 추가
                words.remove(words[index]) # 사용한 것 제거
                

    
    return cnt