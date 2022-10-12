import itertools

N = int(input())
data = list(map(int, input().split()))
operators = list(map(int, input().split()))
op = [] # 들어있는 연산자
result = [] #결과들 저장

for i in range(4):
    for _ in range(operators[i]):
        op.append(i)

# print(op)
# print(list(itertools.permutations(op, N-1)))

for case in list(itertools.permutations(op, N-1)):
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
    result.append(res)

print(max(result))
print(min(result))
