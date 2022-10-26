# 글자: 1, 글자X: 0 8가지 방향 으로 bfs
from collections import deque

M, N = map(int, input().split()) # 세로, 가로
data = []
for _ in range(M):
    data.append(list(map(int, input().split())))
answer = 0

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    data[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        for i in range(8):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if data[nx][ny] == 1:
                q.append((nx, ny))
                data[nx][ny] = 0

for i in range(M):
    for j in range(N):
        if data[i][j] == 1:
            bfs(i, j)
            answer += 1

print(answer)

