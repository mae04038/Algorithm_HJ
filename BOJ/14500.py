'''
개수가 4개일 때 종료, dfs
'''
N, M = map(int, input().split()) # 세로, 가로
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt):
    global res
    cnt += 1
    print("cnt값", cnt, "res값", res)
    if cnt > 4:
        return 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visited[nx][ny]:
            res += data[nx][ny]
            dfs(nx, ny, cnt)


max_sum = 0
res_sum = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            cnt = 1
            res = data[i][j]
            dfs(i, j, cnt)
            print("dfs후 4개 합", res)
            max_sum = max(max_sum, res)

print(max_sum)

