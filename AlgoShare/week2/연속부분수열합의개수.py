def solution(elements):
    answer = 0
    result = set()
    data = []
    data.extend(elements*2)
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            result.add(sum(data[j:j+i]))
    answer = len(result)
    
    return answer