N, M, x, y, K = map(int, input().split()) #세로, 가로, 주사위 처음 좌표, 명령 개수
data = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1] # 동 서 북 남 순으로 - 세로
dy = [1, -1, 0, 0]

def change(dir): #주사위 움직였을 때 바뀐 형태
    top, n1, n2, n3, n4, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = n3, n1, top, bottom, n4, n2
    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = n2, n1, bottom, top, n4, n3
    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = n4, top, n2, n3, bottom, n1
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = n1, bottom, n2, n3, top, n4
    
answer = []
nx, ny = x, y
for order in orders:
    nx = x + dx[order-1]
    ny = y + dy[order-1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    change(order) # 주사위 돌리기
    if data[nx][ny] == 0:
        data[nx][ny] = dice[5]
        answer.append(dice[0])
    else:
        dice[5] = data[nx][ny]
        data[nx][ny] = 0
        answer.append(dice[0])
    x, y = nx, ny # 현재 위치 다시 변경

for ans in answer:
    print(ans)