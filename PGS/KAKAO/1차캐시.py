def solution(cacheSize, cities):
    answer = 0
    cache = []  # LRU 알고리즘: 사용한지 가장 오래된 것을 내보내는 알고리즘

    for i in range(len(cities)):
        cities[i] = cities[i].upper()
    for city in cities:
        if city in cache:  # hit일 경우
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:  # miss일 경우
            answer += 5
            cache.append(city)

            if len(cache) > cacheSize:
                cache.pop(0)

    if cacheSize == 0:
        answer = 5 * len(cities)

    return answer
