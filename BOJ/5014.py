from collections import deque
F, S, G, up, down = map(int, input().split())
# S에서 G로 가는 버튼 수의 최솟값 출력
visited = [False] * (F+1)
visited[0] = True
answer = 0

q = deque()
q.append((S, 0))
visited[S] = True
while q:
    now, cnt = q.popleft()
    if now == G:
        answer = cnt
        break
    for n_now in (now-down, now+up):
        if 1<= n_now <= F and not visited[n_now]:
            q.append((n_now, cnt+1))
            visited[n_now] = True


if not visited[G]:
    print("use the stairs")
else:
    print(answer)



