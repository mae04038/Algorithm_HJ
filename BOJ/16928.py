'''
사다리: 숫자 커짐
뱀: 숫자 작아짐
100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값 
-> 지도에 사다리, 뱀 표시해주기.
-> 뱀 안 만나는 게 좋음
주사위는 1~6
제일 큰 숫자를 가진 곳으로 이동하는 게 이득 
'''
from collections import deque
N, M = map(int, input().split()) # 사다리 개수, 뱀 개수
data = {}
for i in range(1, 101):
    data[i] = 0
cnt = 0
ladder = {}
snake = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
    data[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v
    data[u] = v

def dices(k): # 주사위 돌리기
    

q = deque()
q.append(1)
while q:
    now = q.popleft()




