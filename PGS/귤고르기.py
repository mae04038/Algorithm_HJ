def solution(k, tangerine):
    answer = 0

    gyul = {}
    for t in tangerine:
        if t not in gyul.keys():
            gyul[t] = 1
        else:
            gyul[t] += 1
    # print(gyul)
    sorted_gyul = sorted(gyul.items(), key = lambda x:x[1], reverse=True)
    # print(sorted_gyul)

    for item, n in sorted_gyul:
        if k <= 0:
            break
        if k >= n:
            gyul
            answer += 1
            k -= n
        elif k < n and n >= 1:
            answer += 1
            break

    return answer