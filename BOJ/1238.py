import heapq
N, M, X = map(int, input().split())
data = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(M):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    
def dijkstra(start):
    q = []
    distance = [INF] * (N+1) # 각 도로의 소요시간

    heapq.heappush(q, (0, start)) # 지금까지의 소요시간, 해당도로
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost: # 이미 최소이면 계산할 필요X
            continue
        for node_idx, node_cost in data[now]: # 현재노드를 지나가는 게 더 최소일 때
            final_cost = node_cost + cost

            if distance[node_idx] > final_cost:
                distance[node_idx] = final_cost
                heapq.heappush(q, (final_cost, node_idx))

    return distance

result = 0
for i in range(1, N+1): # i번에서 x까지의 최단시간 + x에서 i번까지의 최단시간
    go_x = dijkstra(i)
    back = dijkstra(X)
    # print("x까지 갈때", go_x)
    # print("x에서 올 때", back)
    result = max(result, go_x[X] + back[i]) 

print(result)