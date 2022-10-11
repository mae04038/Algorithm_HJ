import heapq
import sys
input = sys.stdin.readline
q = []
N = int(input().rstrip())

for _ in range(N):
    num = int(input().rstrip())

    if num == 0: #출력
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, num)


