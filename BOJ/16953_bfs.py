'''그림 참고 : https://velog.io/@joniekwon/Python-%EB%B0%B1%EC%A4%80-16953%EB%B2%88-A-B'''
from collections import deque
a, b = map(int, input().split())
ans = -1

q = deque()
q.append((a, 1))  # 연산결과숫자, 연산횟수
while q:
    num, cnt = q.popleft()
    # print(num, cnt)
    if num == b:
        ans = cnt
        break
    if num*2 <= b:
        q.append((num*2, cnt+1))
    if num*10+1 <= b:
        q.append((num*10+1, cnt+1))

print(ans)
