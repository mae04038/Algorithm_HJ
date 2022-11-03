# 우선순위큐: https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-13549.-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88-3-by-Python
from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001 # 방문처리 -> 메모리초과 해결
q = deque()
q.append((N, 0)) # 위치, 걸린 시간
visited[N] = 1
while q:
    res, time = q.popleft()
    if res == K:
        answer = time
        break
    if (0<= res*2 <= 100000) and not visited[res*2]:
        q.append((res*2, time))
        visited[res*2] = 1
    if (0 <= res - 1 <= 100000) and not visited[res-1]:
        q.append((res-1, time+1))
        visited[res-1] = 1
    if (0 <= res + 1 <= 100000) and not visited[res+1]:
        q.append((res+1, time+1))
        visited[res+1] = 1

print(answer)