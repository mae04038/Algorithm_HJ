from collections import deque
N, M, K = map(int, input().split()) #세로, 가로 음쓰개수
data = [['.']*M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    data[x-1][y-1] = '#'
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    data[i][j] = '.'
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0  or ny >= M:
                continue
            if data[nx][ny] == '#':
                data[nx][ny] = '.'
                q.append((nx, ny))
                # print("큐에 넣기", nx, ny)
                cnt += 1
                
    return cnt

answer = []
for i in range(N):
    for j in range(M):
        if data[i][j] == '#':
            # print("음쓰위치", i, j)
            size = bfs(i, j)
            answer.append(size)

# print(answer)
print(max(answer))