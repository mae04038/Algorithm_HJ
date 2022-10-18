from collections import deque
import sys
input = sys.stdin.readline


def dijkstra(start):
    global graph, visited, distance
    q = deque()
    q.append(start)
    distance[start] = 0
    visited[start] = True
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                distance[node] = min(distance[now] + 1, distance[node])
                visited[node] = True
                q.append(node)


N, M, K, X = map(int, input().split())  # 도시개수, 도로개수, 거리정보, 출발도시
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# x에서 도달할 수 있는 도시들 중 최단거리가 K인 곳 찾기
distance = [1e9] * (N+1)
visited = [False] * (N+1)
dijkstra(X)

# print(distance)
cnt = 0
for i in range(len(distance)):
    if distance[i] == K:
        print(i)
    else:
        cnt += 1

if cnt == N+1:
    print(-1)
