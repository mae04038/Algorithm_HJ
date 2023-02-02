import copy
n, m, k, c = map(int, input().split())  # 격자 크기, 박멸진행년수, 제초제 범위, 제초제 남아있는 년수
forest = [list(map(int, input().split())) for _ in range(n)]  # 나무 표시 좌표
forest_spread = [[0] * n for _ in range(n)]  # 나무들이 번식할 때 활용하는 좌표
pest = [[0] * n for _ in range(n)]  # 제초제 뿌린 현황 표현 (남은 년수도 표기)

answer = 0  # m년 동안 박멸한 나무의 그루

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
dia = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # 대각선 방향


def not_in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    else:
        return False


def step1_grow():
    for x in range(n):
        for y in range(n):
            if forest[x][y] <= 0:  # 나무가 없거나 벽이면
                continue
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if not_in_range(nx, ny):
                    continue
                if forest[nx][ny] > 0:  # 인접한 나무가 있으면
                    forest[x][y] += 1


def step2_spread():
    global forest_spread
    for x in range(n):
        for y in range(n):
            forest_spread[x][y] = 0

    for x in range(n):
        for y in range(n):
            if forest[x][y] <= 0:  # 현재 위치가 빈칸이거나 벽이면
                continue

            # 현재 위치에 나무가 있으면 번식할 곳 찾기(인접 방향)
            empty_cnt = 0
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if not_in_range(nx, ny):
                    continue
                if pest[nx][ny] > 0:  # 제초제가 남아있으면
                    continue
                if forest[nx][ny] == 0:  # 빈 칸이면 번식가능하므로 +1
                    empty_cnt += 1
            # 빈 칸으로 번식하기
            if empty_cnt == 0:
                continue
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if not_in_range(nx, ny):
                    continue
                if pest[nx][ny] > 0:  # 제초제가 남아있으면
                    continue
                if forest[nx][ny] == 0:  # 빈 칸이면 번식가능하므로 +1
                    forest_spread[nx][ny] += forest[x][y] // empty_cnt

    # forest 업데이트 해주기 (번식 포함)
    for x in range(n):
        for y in range(n):
            forest[x][y] += forest_spread[x][y]


def step3_check_max_kill():
    max_cnt = 0  # 가장 많이 박멸되는 나무 수
    max_x, max_y = 0, 0

    for x in range(n):
        for y in range(n):
            if forest[x][y] <= 0:
                continue

            # 대각선 방향으로 박멸 가능 나무 개수 더해주기
            kill_cnt = forest[x][y]
            for dx, dy in dia:
                for distance in range(1, k+1):
                    nx, ny = x + (dx * distance), y + (dy * distance)
                    if not_in_range(nx, ny):
                        break
                    if forest[nx][ny] <= 0:
                        break
                    kill_cnt += forest[nx][ny]
            # max값 최대이면 업데이트
            if max_cnt < kill_cnt:
                max_cnt = kill_cnt
                max_x, max_y = x, y

    global answer
    answer += max_cnt

    return max_x, max_y


def reduce_pest_time():
    for x in range(n):
        for y in range(n):
            pest[x][y] -= 1


def step3_kill(max_x, max_y):
    # 대각선 방향으로 제초제 뿌리기
    pest[max_x][max_y] = c
    forest[max_x][max_y] = 0

    for dx, dy in dia:
        for distance in range(1, k+1):
            nx, ny = max_x + (dx * distance), max_y + (dy * distance)
            if not_in_range(nx, ny):
                break
            if forest[nx][ny] <= 0:  # 벽이거나 나무가 없으면 뿌리고 멈추기
                pest[nx][ny] = c
                break
            pest[nx][ny] = c
            forest[nx][ny] = 0


for _ in range(m):
    # 1. 성장
    step1_grow()

    # 2. 번식
    step2_spread()

    # 3-1. 가장 많이 박멸되는 칸 찾기
    max_x, max_y = step3_check_max_kill()
    # 3-2. 제초제 1년 감소
    reduce_pest_time()
    # 3-3. 박멸시키기
    step3_kill(max_x, max_y)

print(answer)
