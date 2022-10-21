def solution(clothes):
    answer = len(clothes)
    data = {}
    for name, types in clothes:
        if types not in data.keys():
            data[types] = []
            data[types].append(name)
        else:
            data[types].append(name)
    print(data)
    
    res = 1
    for k in data.keys():
        res *= len(data[k]) + 1 # 안 입는 경우 포함
    
    res -= 1 #전부 안 입는 경우 제외
    
    answer = res
    
    return answer