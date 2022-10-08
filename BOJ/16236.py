'''
0: 빈칸, 9: 아기상어위치, 1~8: 물고기 크기
처음 아기상어의 크기는 2, 자신보다 큰 물고기 있으면 못 지나감.
아기상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가
abs사용 -> 거리랑 칸 수 똑같.
'''
from collections import deque
dx = [-1, 0, 1, 0]  # 상 좌 하 우 순으로
dy = [0, -1, 0, 1]

N = int(input())
data = []
shark = [0, 0, 0]  # x좌표, y좌표, 상어크기
fishes = []
for i in range(N):
    info = list(map(int, input().split()))
    data.append(info)
    for j in range(N):
        if info[j] == 9:
            shark = [i, j, 2]  # 최초 아기상어 위치
        elif info[j] != 0:
            fishes.append((i, j))  # 물고기 좌표 넣어주기

time = 0  # 시간 계산
eat = 0  # 잡아먹은 물고기 개수


def find_fish():
    exist = False
    now_x, now_y, now_size = shark[0], shark[1], shark[2]
    print(now_x, now_y, now_size)
    for i in range(4):
        nx, ny = now_x + dx[i], now_y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if data[nx][ny] < now_size and data[nx][ny] != 0:
            data[now_x][now_y] = 0
            time += 1
            eat += 1
            exist = True
            if eat == now_size:
                shark[2] = now_size + data[nx][ny]
            shark[0], shark[1] = nx, ny
            fishes.remove((nx, ny))
    return exist


def find_min_distance():  # 현재 상어 위치에서 제일 가까운 물고기 위치 구하기
    dist = 1000
    now_x, now_y, now_size = shark[0], shark[1], shark[2]
    fish_x, fish_y = -1, -1
    for x, y in fishes:
        now_dist = abs(now_x - x) + abs(now_y - y)
        if now_dist < dist:
            dist = now_dist
            fish_x, fish_y = x, y  # 잡아먹을 물고기 위치
    return fish_x, fish_y, dist


while len(fishes) != 0:  # 물고기를 다 먹었을 때 종료
    fish_x, fish_y = -1, -1
    dist = 0
    if find_fish():  # 상 좌 하 우 방향에 물고기 있는지 확인
        print("4방향에 물고기 존재")
        break
    else:
        print("가까이에 존재하지 않음")
        fish_x, fish_y, dist = find_min_distance()  # 잡아먹을 물고기 위치
        time += dist  # 이동한 칸 수만큼 시간 더해주기
        eat += 1
        if eat == shark[2]:
            shark[2] += 1
        fishes.remove((fish_x, fish_y))
        shark[0], shark[1] = fish_x, fish_y


print(time)
