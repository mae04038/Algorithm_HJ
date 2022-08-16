'''
1 : 익은 토마토
0 : 익지 않은 토마토
-1 : 토마토가 들어있지 않은 칸
하루가 지나면 인접한 곳이 익게 됨. -> 1 위치가 여러개일 경우 동시에 진행됨. -> 이전위치+1 해주기 때문에 큐 하나로 해도됨.
며칠이 지나야 다 익게 되는지 최소 일수 구하기, 모두 익지 못하는 상황엔 -1 출력
'''
from collections import deque
M, N = map(int, input().split()) # 가로칸 개수, 세로칸개수
tomato = []
tomato_ripen = []
cnt_zero = 0
ans = 0
q = deque()
for i in range(N):
    tomato.append(list(map(int, input().split())))
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j)) # 익은 토마토 위치 큐에 넣기
        elif tomato[i][j] == 0:
            cnt_zero += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt_ripen = len(tomato_ripen) # 처음에 입력받은 익은 토마토위치 개수

while q:
    now_x, now_y = q.popleft()
    for i in range(4):
        nx, ny = now_x + dx[i], now_y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[now_x][now_y] + 1
            q.append((nx, ny))
            cnt_zero -= 1

for i in range(N):
    ans = max(max(tomato[i]), ans)
if cnt_zero == 0:
    print(ans-1)
elif cnt_ripen == N*M:
    print(0)
else:
    print(-1)
