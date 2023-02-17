import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 비용, 위치 순 - 비용이 작은 게 먼저 나옴
    distance[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for road in roads[now]: # 현재위치 거쳐서 갈 때
            dist = cost + road[1]
            if dist < distance[road[0]]:
                distance[road[0]] = dist
                heapq.heappush(q, (dist, road[0]))



N, D = map(int, input().split())
roads = [[] for _ in range(D+1)] 
INF = int(1e9)
distance = [INF] * (D+1)

for i in range(D):
    roads[i].append((i+1, 1))
for _ in range(N):
    a, b, c = map(int, input().split())
    if b > D:
        continue
    roads[a].append((b, c)) # b까지의 비용이 c

dijkstra(0)
print(distance[D])


