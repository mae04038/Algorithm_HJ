from collections import deque
N, K = map(int, input().split())
q = deque()
result = []
for i in range(1, N+1):
    q.append(i)
# print(q)
print("<", end="")
while q:
    for i in range(K-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end="")
    if q:
        print(", ", end="")
print(">")

'''
while q:
    q.rotate(-(K-1))
    result.append(q.popleft())

for i in range(N):
    if i == 0:
        print("<%d, "%result[i], end="")
    elif i == N-1:
        print("%d>"%result[i], end="")
    else:
        print("%d, "%result[i], end="")
'''