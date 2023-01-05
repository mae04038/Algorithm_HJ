def solution(data, col, row_begin, row_end):
    answer = 0
    result = []
    sortedData = sorted(data, key = lambda x : (x[col-1], -x[0]))

    # print(sortedData)
    res = 0
    for i in range(row_begin-1, row_end):
        s_i = 0
        for j in sortedData[i]:
            s_i += j % (i+1)
        answer = answer ^ s_i
        
    
    return answer