def solution(cacheSize, cities):
    answer = 0
 
    cache = []
    for city in cities:
        city = city.lower()
        
        if city in cache:
            answer += 1 #cache hit
            cache.pop(cache.index(city))
            cache.append(city) #가장 최근에 사용했으므로 맨 뒤에 추가
        else:
            answer += 5 #cache miss
            if cacheSize==0:
                pass
            elif cacheSize!=0 and len(cache) < cacheSize:
                cache.append(city)
            else:
                if len(cache)>0:
                    cache.remove(cache[0])
                cache.append(city)
     
    
    
    
    return answer