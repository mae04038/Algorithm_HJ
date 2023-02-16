def solution(k, tangerine):
    answer = 0 # 서로 다른 종류 개수
    
    gyul = {}
    for t in tangerine:
        if t not in gyul.keys():
            gyul[t] = 1
        else:
            gyul[t] += 1
    sortedGyul = sorted(gyul.items(), key = lambda x:x[1], reverse=True)
    cnt = 0
    for g, g_cnt in sortedGyul:
        if cnt < k:
            cnt += g_cnt
            answer += 1
    
    return answer