import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) #노드개수
INF = int(1e9)
graph = [[] for _ in range(N+1)]
answer = []
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for start in range(1, N+1): # start에서 다른 노드들까지의 거리 distance[i]: start에서 i까지의 거리.
    visited = [False] * (N+1)
    distance = [INF] * (N+1)

    visited[start] = True
    distance[start] = 0
    distance[0] = 0

    q = deque()
    q.append(start) # 시작노드 
    while q:
        now = q.popleft()
        for nd in graph[now]: # nd[0]: 노드 , nd[1]: 거리 비용  
            if not visited[nd[0]]:
                distance[nd[0]] = min(distance[nd[0]], distance[now] + nd[1])
                q.append(nd[0])
                visited[nd[0]] = True
    print("시작노드: ", start, ", 최종거리비용 : ", distance)
    answer.append(sum(distance))
for d in answer:
    print(d)    