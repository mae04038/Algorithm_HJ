from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


idx = 1
while True:
    N = int(input())
    if N == 0:
        break
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    visited = [[False]*N for _ in range(N)]
    tmp = [[1e9]*N for _ in range(N)]
    tmp[0][0] = data[0][0]

    q = deque()
    q.append((0, 0)) # x좌표, y좌표, 잃은 금액
    visited[0][0] = True
    while q:
        x, y = q.popleft()
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[nx][ny]:
                if tmp[nx][ny] > tmp[x][y] + data[nx][ny]:
                    tmp[nx][ny] = tmp[x][y] + data[nx][ny] 
                    q.append((nx, ny))
    


    print("Problem %d: %d" %(idx,tmp[N-1][N-1]))
    idx += 1
