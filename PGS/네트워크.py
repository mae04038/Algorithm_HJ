def dfs(start, visited, graph):
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            dfs(node, visited, graph)

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, graph)
            answer += 1



    return answer