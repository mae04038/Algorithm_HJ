from collections import deque
def solution(n, results):
    answer = 0

    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]

    for result in results:
        win[result[0]].append(result[1])
        lose[result[1]].append(result[0])

    for i in range(1, n+1): # 각각의 경우에서 visited 다 완료한 경우 answer + 1
        visited = [False] * (n+1)
        visited[0] = visited[i] = True

        for nodes in [win, lose]: # win이랑 lose 둘 다 확인
            q = deque()
            q.append(i)
            while q:
                idx = q.popleft()
                for nd in nodes[idx]:
                    if not visited[nd]:
                        visited[nd] = True
                        q.append(nd)
        if False not in visited:
            answer += 1

    return answer