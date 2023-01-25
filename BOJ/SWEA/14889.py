def dfs(depth, idx):
    global min_diff

    if depth == N//2:  # 팀 나눠졌으면 능력치 계산
        start_power, link_power = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_power += data[i][j]
                elif not visited[i] and not visited[j]:
                    link_power += data[i][j]
       
        min_diff = min(min_diff, abs(start_power - link_power))  # 다 탐색해보고 최솟값 업데이트
        return

    for i in range(idx, N):  # 스타트, 링크 팀 나눠주도록 dfs
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

min_diff = int(1e9)
visited = [False] * N

dfs(0, 0)  # 팀 개수, idx

print(min_diff)
