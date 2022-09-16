from itertools import permutations
def solution(k, dungeons):
    answer = 0
    permu = list(permutations(dungeons, len(dungeons)))
    result = []
    for i in range(len(permu)):
        case = permu[i]
        cnt = 0
        total = k
        for j in range(len(case)):
            if total >= case[j][0]:
                total -= case[j][1]
                cnt += 1
        result.append(cnt)


    return max(result)