'''
참고 : https://justkode.kr/algorithm/python-dijkstra
'''
V, E = map(int, input().split())
start = int(input()) #시작 정점
INF = int(1e9)
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [INF] * (V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 방향 존재

def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, V+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 #시작노드는 0으로 초기화
    visited[start] = True

    for nd in graph[start]: #시작노드와 연결된 노드들의 거리 입력
        distance[nd[0]] = nd[1]

    for _ in range(V-1): 
        now = get_smallest_node() #거리가 구해진 노드들 중 가장 최소비용거리인 곳 선택
        visited[now] = True # 방문처리

        for j in graph[now]: # now가 현재노드(이전시점에서 가장 최소비용인 곳)
            if distance[now] + j[1] < distance[j[0]] : #기존 입력값보다 더 작은 비용일때
                distance[j[0]] = distance[now] + j[1]


dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

