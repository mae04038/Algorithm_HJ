from collections import deque
def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n+1)]
    for eg in edge:
        graph[eg[0]].append(eg[1])
        graph[eg[1]].append(eg[0])
    visited = [False] * (n+1)
    distance = [1e9] * (n+1)

    q = deque()
    q.append(1)
    distance[0], distance[1] = 0, 0
    while q:
        now = q.popleft()
        for nd in graph[now]:
            if not visited[nd]:
                distance[nd] = min(distance[nd], distance[now] + 1)
                q.append(nd)
                visited[nd] = True
    print(distance)
    for cnt in distance:
        if cnt == max(distance): answer += 1


    return answer