from collections import deque
N = int(input())
miro = list(map(int, input().split()))
answer = -1

visited = [False] * N
q = deque()
visited[0] = True  # 메모리초과 - 해결코드
q.append((miro[0], 0, 0))  # 값, 인덱스, 카운트
while q:
    now_value, now_index, cnt = q.popleft()
    if now_index == N-1:
        answer = cnt
        break

    for i in range(1, now_value+1):
        if now_index+i < N and not visited[now_index+i]:
            q.append((miro[now_index+i], now_index+i, cnt+1))
            visited[now_index+i] = True

print(answer)
