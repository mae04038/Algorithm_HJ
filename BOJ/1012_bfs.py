'''
1 : 배추
0 : 배추 X
최소 몇 마리의 배추흰지렁이가 필요한지
'''
from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if cabbage[next_x][next_y] == 1 and not visited[next_x][next_y]:
                q.append((next_x, next_y))
                visited[next_x][next_y] = True
    return


for _ in range(T):
    ans = 0
    M, N, K = map(int, input().split())
    cabbage = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        m, n = map(int, input().split())
        cabbage[n][m] = 1

    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and not visited[i][j]:
                bfs(i, j, visited)
                ans += 1
    print(ans)