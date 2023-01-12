'''
collection모듈의 deque 자료형 : 리스트 회전문제 deque.rotate() 사용 
'''
from collections import deque

def roatate_right(num, d): #시계방향 회전
    if num > 4 or gears[num-1][2] == gears[num][6]: #범위 벗어나거사 같은 극이면 회전X
        return
    if gears[num-1][2] != gears[num][6]:
        roatate_right(num+1, -d)
        gears[num].rotate(d)

def rotate_left(num, d): #반시계방향 회전 
    if num <= 0 or gears[num+1][6] == gears[num][2]:
        return
    if gears[num+1][6] != gears[num][2]:
        rotate_left(num-1, -d)
        gears[num].rotate(d)

gears = {}
for i in range(1, 5):
    gears[i] = deque(map(int, input())) # input()이 입력을 문자열로 저장하고 차례로 int()적용 -> 각각 정수로 바뀜

K = int(input())  # 회전횟수
for _ in range(K):
    n, dir = map(int, input().split()) # 톱니바퀴 번호, 회전방향
    
    roatate_right(n+1, -dir) # 우선 반대방향으로 돌린다고 가정했을 때 함수 들어가서 여부 확인
    rotate_left(n-1, -dir)

    gears[n].rotate(dir) # 1 이면 시계방향 -1이면 반시계방향

ans = 0
for i in range(4):
    if gears[i+1][0] == 1:
        # print(2**i)
        ans += 2**i
print(ans)
