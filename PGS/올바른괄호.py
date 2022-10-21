def solution(s):
    answer = True
    data = list(s)
    # print(data)
    stack = []

    if data[0] == ')': return False # 테케 2, 6: 효율성 실패 해결 코드

    for d in data:
        if d == '(':
            stack.append(d)
        if d == ')' and len(stack) != 0:
            stack.pop()


    if len(stack) == 0:
        answer = True
    else:
        answer = False

    return answer

