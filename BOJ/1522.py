import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리비용, 위치
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in data[now]: # now거쳐서 갈 때
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



N, D = map(int, input().split()) #지름길, 고속도로 길이
data = [[] for _ in range(D+1)]
distance = [1e9] * (D+1)

for i in range(D):
    data[i].append((i+1, 1))
for _ in range(N):
    start, end, cost = map(int, input().split())
    if end > D:
        continue
    data[start].append((end, cost))

dijkstra(0)
print(distance[D])