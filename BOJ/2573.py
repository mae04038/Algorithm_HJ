# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(몇 년 걸리는지)
# 시간초과 -> pypy제출함

from collections import deque
import copy, sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)] # 원래 정보 저장

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0 # 시간 저장

def cnt_surround_ice(x, y):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if change_data[nx][ny] <= 0: ### 수정해야하는 부분
            cnt += 1
    data[x][y] = change_data[x][y] - cnt 
    if data[x][y] <= 0:
        data[x][y] = 0

def bfs(x, y, visited):
    # print("좌표", x, y)
    q = deque()
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0  or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and data[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))
    return

while True:

    change_data = copy.deepcopy(data) # 바뀐 정보 저장
    
    for i in range(N):
        for j in range(M):
            if change_data[i][j] > 0:
                cnt_surround_ice(i, j)
    # print(data)

    # 덩어리 수 세기
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if data[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, visited) # 덩어리 세기
                cnt += 1
                # print(visited)
    # print("개수 세기 끝")
    answer += 1
    if cnt >= 2:
        break
    if sum(map(sum, data[1:-1])) == 0:
        answer = 0
        break


print(answer)
