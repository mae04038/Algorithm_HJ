import heapq
def solution(operations):
    answer = []
    q = [] # 오름차순 정렬됨.

    for operation in operations:
        op, num = operation.split(" ")
        if op == "I":
            heapq.heappush(q, int(num))
        if len(q) == 0: # 힙이 비어있을 때 출력을 요구하는 경우
            continue
        else:
            if op == "D" and num == "-1": # 최솟값 삭제
                heapq.heappop(q)
            if op == "D" and num == "1": # 최댓값 삭제
                del q[-1]
        print(q)


    if len(q) == 0:
        answer = [0, 0]
    else:
        q.sort()
        answer = [q[-1], q[0]]

    return answer