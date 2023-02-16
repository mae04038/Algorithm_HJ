''' 3명 이상이 한 팀 (무조건 1, 2, 3 존재)'''
from collections import deque
import copy
n, m, k = map(int, input().split())  # 격자 크기, 팀 개수(5개 최대), 라운드 수
data = [list(map(int, input().split())) for _ in range(n)]
move_data = copy.deepcopy(data)
rotate = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 4로 나눈 나머지 에 따라서 공 던지는 방향
people = [[] for _ in range(m)]  # 각각 머리사람위치, 중간, 꼬리사람위치 넣어주기
answer = 0

r = 0  # 현재 라운드
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def step0_location():
    cnt = 0
    for x in range(n):
        for y in range(n):
            if data[x][y] == 1:
                people[cnt].append((x, y))
                cnt += 1
    # print(people)
    visited_loc = [[False] * n for _ in range(n)]
    for i in range(m):
        x, y = people[i][0]
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if (data[nx][ny] == 2 or data[nx][ny] == 3) and not visited_loc[nx][ny]:
                    visited_loc[nx][ny] = True
                    people[i].append((nx, ny))
                    q.append((nx, ny))
    # print(people) # 확인용


def step1_move(team):
    # print(team) # 확인용
    after_team = []
    head_x, head_y = team[0]
    for i in range(4):
        nx, ny = head_x + dx[i], head_y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if data[nx][ny] == 4 or data[nx][ny] == 3:  # 팀원이 이동경로 길이랑 같을 수도 있음
            after_team.append((nx, ny))
    prev_x, prev_y = head_x, head_y
    for i in range(1, len(team)):
        nx, ny = prev_x, prev_y
        after_team.append((nx, ny))
        prev_x, prev_y = team[i]
    return after_team


def step2_get_ball_path(r):
    path = []  # 공이 지나가는 위치들
    side, extra = divmod(r, n)  # 라운드 수를 n으로 나누기 -> 몫: 던져지는 방향 결정, 나머지
    if side % 4 == 0:  # 우
        for y in range(n):
            path.append((extra, y))
    elif side % 4 == 1:  # 상
        for x in range(n-1, -1, -1):
            path.append((x, extra))
    elif side % 4 == 2:  # 좌
        for j in range(n-1, -1, -1):
            path.append((n-extra, j))
    elif side % 4 == 3:
        for x in range(n):
            path.append((x, n-extra))
    return path

def step3_get_score(ball_path, teams):
    for path in ball_path: # 공 던져지는 경로 순
        for n in range(len(teams)):
            for idx, pos in enumerate(teams[n]):
                if tuple(pos) == path: # 공 던져지는 위치 순이므로 자동으로 가장 먼저 맞은 사람
                    teams[n] = teams[n][::-1] # 머리사람 꼬리사람 위치 바뀜
                    return (idx+1)*(idx+1) # 사람 만나면 끝, 리턴
    return 0

def step4_set_data(people):
    for n in range(m):
        for idx, pos in enumerate(people[n]):
            if idx == 0:
                data[pos[0]][pos[1]] = 1
            elif idx == len(people[n])-1:
                data[pos[0]][pos[1]] = 3
            else:
                data[pos[0]][pos[1]] = 2
    return data

while r < k:  # 매 라운드마다

    # 0. 각 팀의 위치 확인(머리사람, 꼬리사람)
    step0_location()
    # print(people)

    # 1. 각 팀 머리사람 따라서 한 칸 이동
    for i in range(m):
        people[i] = step1_move(people[i])  # 이동한 후 위치 갱신
    # print(people)

    # 2. 공 던지기
    # 2-1. 공 던져지는 경로 확인 - 사람 만나면 위치 리턴, 아니면 (-1, -1)리턴
    ball_path = step2_get_ball_path(r)
    # print(ball_path)

    # 3. 공 던지는 중에 사람 만나면 점수 얻기. (팀 내에서 몇 번재 선수인지-제곱)
    # 3-1. 점수 획득한 팀은 머리사람 꼬리사람 바꾸기 (이동 방향 바뀜)
    answer += step3_get_score(ball_path, people)

    # 이동위치에 따라 지도 다시 설정 (머리사람, 꼬리사람 위치)
    data = step4_set_data(people)
    r += 1  # 현재 라운드

print(answer)