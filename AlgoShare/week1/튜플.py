def solution(s):
    answer = []

    data = s[:-2].replace('{', '').replace(',', ' ').split('}')
    # print(data)
    res = []
    for d in data:
        res.append(d.split())
    # print(res)

    res = sorted(res, key=lambda x:len(x)) # 길이가 작은 것부터 고려
    for i in range(len(res)):
        for j in res[i]:
            if int(j) not in answer:
                answer.append(int(j))


    return answer
