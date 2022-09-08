from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0]) # 세로, 가로
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    # 정확성 12, 15, 16 통과못한 코드
    # if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0: # 상대팀진영에 도착할 수 없는 경우
    #     answer = -1
    #     return answer
    
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1 and not visited[nx][ny]:
                maps[nx][ny] += maps[x][y]
                visited[nx][ny] = True
                q.append((nx, ny))
    
    answer = maps[n-1][m-1]
    
    return -1 if answer == 1 else answer