# 50미터 당 맥주 한 병씩 - 한박스에 맥주 20개 => 50*20 = 1000미터
# 락 페스티발까지 도착할 수 있는지를 확인하는 문제
from collections import deque
t = int(input())

def bfs():
    q = deque()
    q.append((home_x, home_y))
    while q:
        cx, cy = q.popleft()
        if abs(cx - fest_x) + abs(cy - fest_y) <= 1000:
            return "happy"
        for i in range(n):
            if not visited[i]:
                nx, ny = super[i][0], super[i][1]
                if abs(nx - cx) + abs(ny - cy) <= 1000:
                    q.append((nx, ny))
                    visited[i] = True
    return "sad"

for _ in range(t):
    n = int(input()) # 편의점 개수
    super = []
    home_x, home_y = map(int, input().split()) # 상근이네 집
    for _ in range(n): super.append(list(map(int, input().split())))  # 편의점
    fest_x, fest_y = map(int, input().split()) # 락 페스티발
    answer = ""
    visited = [False] * n

    print(bfs())

