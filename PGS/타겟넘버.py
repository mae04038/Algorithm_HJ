from collections import deque
def solution(numbers, target):
    answer = 0
    
    n = len(numbers)

    q = deque([])
    q.append(0)
    
    for i in range(n):
        data = []
        while q:
            a = q.popleft()
            data.append(a+numbers[i])
            data.append(a-numbers[i])
        # print("while문 끝", q)
        for j in range(len(data)):
            q.append(data[j])
        # print(q)
    # print(q)
    # print(q.count(target))

       
    return q.count(target)