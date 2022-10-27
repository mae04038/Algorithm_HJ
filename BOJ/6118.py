from collections import deque
N, M = map(int, input().split()) #헛간개수, M개의 양방향 길.
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
distance = [1e9] * (N+1) # 거리비용 저장
visited = [False] * (N+1)

q = deque()
visited[1] = True
for nd in graph[1]:
    distance[nd] = 1 # 1번 헛간이랑 연결된 곳의 거리비용
    q.append(nd)
    visited[nd] = True

while q:
    now = q.popleft()
    for nd in graph[now]:
        if not visited[nd]:
            distance[nd] = min(distance[now]+1, distance[nd])
            q.append(nd)
            visited[nd] = True

hide = 0
# print(max(distance[2:]))
for i in range(len(distance)):
    if distance[i] == max(distance[2:]):
        hide = i
        # print(hide)
        break
print(hide, distance[hide], distance.count(distance[hide]))