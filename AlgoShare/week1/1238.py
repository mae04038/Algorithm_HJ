import heapq

N, M, X = map(int, input().split())
road = [[] for _ in range(N+1)]
INF = int(1e9)
for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append((b, c))
# print(road)

result = [] # 각각 X에서 왕복 걸리는 시간 저장하는 리스트

def dijkstra(start):
    q = []
    distance = [INF]*(N+1)

    heapq.heappush(q, (0, start)) #지금까지의 소요시간, 해당도로
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for node_idx, node_cost in road[now]: # 현재노드를 지나가는 게 더 최소
            final_cost = cost + node_cost
            if distance[node_idx] > final_cost:
                distance[node_idx] = final_cost
                heapq.heappush(q, (distance[node_idx], node_idx))

    return distance


for i in range(1, N+1):
    go_x = dijkstra(i) # i에서 다른 노드들까지의 최단거리 리스트 
    back = dijkstra(X) # x에서 다른 노드들까지의 최단거리 리스트

    result.append(go_x[X]+back[i])

print(max(result))
