import math
def solution(n, stations, w):
    answer = 0
    w_range = w*2 + 1 # 기지국 위치 + 영향 버뮈
    start = 1
    for st in stations:
        end = st - w
        house = end - start
        answer += math.ceil(house / w_range)
        start = st + w + 1

    if start <= n:
        house = n - start + 1
        answer += math.ceil(house/w_range)

    return answer