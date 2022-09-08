from collections import deque

def bfs(x, y, maps):
    n, m = len(maps), len(maps[0]) # 세로, 가로
    q = deque()
    q.append((x, y))
    while q:
        print("큐 상태",q)
        now_x, now_y = q.popleft()
    
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0:
                continue
            else:
                maps[nx][ny] += maps[now_x][now_y]
                q.append((nx, ny))
    return 
        

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0]) # 세로, 가로
    
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0: # 상대팀진영에 도착할 수 없는 경우
        answer = -1
        return answer
    maps[0][0] = 1
    print(maps)
    bfs(0, 0, maps)
    answer = maps[n-1][m-1]
    
    return answer

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))