import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
stop1, stop2 = map(int, input().split())

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance = [1e9] * (N+1)
    distance[start], distance[0] = 0, 0

    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]: continue

        for nd in graph[now]:
            if distance[now] + nd[1] < distance[nd[0]]:
                distance[nd[0]] = distance[now] + nd[1]
                heapq.heappush(q, (distance[nd[0]], nd[0]))

    # print(distance)

    return distance[end]
    

path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, N)
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, N)

if path1 >= 1e9 and path2 >= 1e9:
    print(-1)
else:
    print(min(path1, path2))
