# 수학 다항식 응용
def solution(clothes):
    answer = 1

    info = {}
    for cloth in clothes:
        if cloth[1] not in info.keys():
            info[cloth[1]] = []
            info[cloth[1]].append(cloth[0])
        else:
            info[cloth[1]].append(cloth[0])
    # print(info)

    for key in info.keys():
        answer *= 1 + len(info[key])

    return answer - 1
