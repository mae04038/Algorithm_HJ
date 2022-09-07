def solution(s):
    answer = ''

    data = list(map(int,s.split()))
    # print(data)
    max_value = max(data)
    min_value = min(data)
    # print(max_value, min_value)

    answer = str(min_value) + " " + str(max_value)
    return answer

