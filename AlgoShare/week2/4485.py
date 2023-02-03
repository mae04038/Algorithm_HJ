import heapq
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
T = 1
while True:
    N = int(input())
    if N == 0:
        break
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = 0

    q = []
    heapq.heappush(q, (data[0][0], 0, 0))
    visited[0][0] = True
    while q:
        cost, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            answer = cost
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(q, (cost+data[nx][ny], nx, ny))


    print("Problem {}: {}".format(T, answer))
    T += 1

    