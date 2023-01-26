from collections import deque
N, K = map(int, input().split()) # 현재위치, 목표위치
ans = 0
visited = [False] * 100001 # 무한반복 없애기 위함
q = deque()
q.append((N, 0)) # 현재 값, 소요시간
visited[N] = True

while q:
    now, time = q.popleft()
    
    if now == K:
        ans = time
        break
    if (0 <= now*2 <= 100000) and not visited[now*2]:
        q.appendleft((now*2, time)) # 곱셈 우선순위 고려해서 appendleft
        visited[now*2] = True
    if (0 <= now+1 <= 100000) and not visited[now+1]:
        q.append((now+1, time+1))
        visited[now+1] = True
    if (0 <= now-1 <= 100000) and not visited[now-1]:
        q.append((now-1, time+1))
        visited[now-1] = True
    
    
    
print(ans)