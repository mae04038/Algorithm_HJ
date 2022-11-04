# N-1, M-1 이 최종지점  0: 빈방, 1: 벽
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
M, N = map(int, input().split()) # 가로, 세로
data = []
for _ in range(N):
    data.append(list(input()))
distance = [[-1] * M for _ in range(N)]

def bfs(i, j):
    q = deque()
    q.append((i, j)) # ㅌ좌표, y좌표, 부슨 벽의 개수
    distance[i][j] = 0

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if distance[nx][ny] == -1:
                if data[nx][ny] == '0':
                    distance[nx][ny] = distance[x][y]
                    q.appendleft((nx, ny)) #비용이 적은걸 우선적으로 탐색하기 위해 앞쪽에 넣어주기
                if data[nx][ny] == '1':
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))


bfs(0, 0) # 시작
print(distance[N-1][M-1])
