def solution(people, limit):
    answer = 0
    people.sort(reverse=True) # [80, 70, 50, 50]
    # 무거운 사람부터 채우고 가벼운 사람 채워 넣기
    for index, i in enumerate(people):
        if i + people[-1]<= limit: # 같이 탈수 있을때
            people.pop()
            answer+=1
        else:
            answer+=1

    return answer