'''
순열 + bfs 사용
'''
import itertools
from collections import deque

N = int(input())
data = list(map(int, input().split()))
operators = list(map(int, input().split()))
op = [] # 들어있는 연산자
result = [] #결과들 저장


for i in range(4):
    for _ in range(operators[i]):
        op.append(i)

cases = list(itertools.permutations(op, N-1))
q = deque(cases)
# print(q)
# print(op)
# print(list(itertools.permutations(op, N-1)))
max_res = -1e9
min_res = 1e9

while q:
    case = q.popleft()
    res = data[0]
    for i in range(N-1):
        if case[i] == 0:
            res += data[i+1]
        elif case[i] == 1:
            res -= data[i+1]
        elif case[i] == 2:
            res *= data[i+1]
        else:
            if res < 0:
                res = -res
                res //= data[i+1]
                res = -res
            else:
                res //= data[i+1]
    max_res = max(max_res, res)
    min_res = min(min_res, res)

print(max_res)
print(min_res)
