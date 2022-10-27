def solution(elements):
    answer = 0
    
    result = set()
    data = elements*2 #똑같은 수열 뒤에 붙여줌
    # print(data)
    
    for i in range(1, len(elements)+1): # 길이가 i인 수열
        for j in range(len(elements)):
            result.add(sum(data[j:j+i]))
    # print(result)
    answer = len(result)
    return answer