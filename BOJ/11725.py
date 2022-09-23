from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
parents = [1] * (N+1)
visited = [False] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
# print(visited)

# 1부터 시작하면서 연결 노드의 부모는 방금 내려온 노드
q = deque()
q.append(1)
while q:
    prev = q.popleft()
    for node in graph[prev]:
        if not visited[node]:
            visited[node] = True
            parents[node] = prev
            q.append(node)
# print(parents)
for i in range(2, N+1):
    print(parents[i])