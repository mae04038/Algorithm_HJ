'''
시간초과 해결 -> 우선순위큐 사용 heapq
'''
import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input()) #시작 정점
INF = 1e9

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 우선순위(거리비용), 값 형태로 넣기
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위(거리비용)가 가장 작은 값이 나옴

        if distance[now] < dist: # 이미 입력된 거리 비용이 현재노드까지의 비용보다 작으면 더 구할 필요X
            continue

        for i in graph[now] : # 현재노드에 연결된 노드들 탐색
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))



dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
