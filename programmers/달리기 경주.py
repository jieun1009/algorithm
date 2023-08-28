def solution(players, callings):
    # 플레이어 호출될때마다 앞자리 사람과 idx 맞바꿈
    result=[0]*len(players)
    arr = {players[i]: int(i) for i in range(len(players))}
    rank = {}

    for i in callings:
        rank = arr[i] #현재 순위
        
        # 순위 바꾸기
        arr[i]-=1 
        arr[players[rank-1]] = rank
        
        # palyers 업데이트
        players[rank], players[rank-1] = players[rank-1] ,players[rank]
        
    for k,v in arr.items():
        result[v]=k
    

    return result