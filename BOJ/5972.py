import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #비용, 시작점 넣어주기
    distance[start] = 0

    while q:
        # print("큐 상태", q)
        dist, cow = heapq.heappop(q) # 거리가 가장 짧은 노드 꺼냄
        # print("최소비용, 소", dist, cow)

        if distance[cow] < dist: #cow까지의 거리가 이미 최소비용이면 굳이 계산할 필요 없으므로
            continue

        for next_cow, next_dist in roads[cow]:
            cost = dist + next_dist # 현재노드를 거쳐서 가는 게 최소비용일 때 distance업데이트, 큐에 삽입
            if cost < distance[next_cow]:
                distance[next_cow] = cost
                heapq.heappush(q, (cost, next_cow))


N, M = map(int, input().split()) # 도착지점, 소들의 길
roads = [[] for _ in range(N+1)]
INF = 1e9

for _ in range(M):
    a, b, c = map(int, input().split())
    roads[a].append((b, c)) # b까지의 비용이 c
    roads[b].append((a, c))

visited = [False] * (M+1)
distance = [INF] * (N+1) # 1번에서 해당 노드까지의 최소거리

dijkstra(1)
# print(distance)
print(distance[-1])

