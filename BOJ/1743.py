import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M, K = map(int, input().split())  # 세로 가로 음쓰개수
data = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    data[r-1][c-1] = 1  # 음쓰 위치는 1로 해줌
# print(data)


def dfs(x, y):
    global trash

    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if data[x][y] == 1:
        trash += 1
        data[x][y] = 0  # 0으로 바꿔주기
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)

    return False


max_trash = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            trash = 0
            dfs(i, j)
            max_trash = max(max_trash, trash)
print(max_trash)
