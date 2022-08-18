'''
어떤 지역의 높이가 주어졌을 때, 안전영역의 최대 개수 구하기.
지역의 높이의 최댓값과 최솟값
각 높이에서의 안전영역개수구한 다음 max 찾기
'''
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
min_h = 101
max_h = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, height):
    global visited
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
            continue
        if data[nx][ny] > height and not visited[nx][ny]:
            dfs(nx, ny, height)
    return


for i in data:
    min_h = min(min(i), min_h)
    max_h = max(max(i), max_h)

result = 0
# 높이가 1이상 100이하이므로 range(max_h+1)
for height in range(max_h+1): # height가 max_h보다 크면 안전영역 0개이므로 계산할 필요X
    safe = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] > height and not visited[i][j]: # 비 높이보다 높고 방문하지 않은 곳일 때 dfs 수행
                dfs(i, j, height)
                safe += 1
            else:
                continue
    # print("높이", height, "안전영역개수", safe)
    result = max(result, safe)

print(result)
