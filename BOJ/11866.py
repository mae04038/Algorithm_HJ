N, K = map(int, input().split())
data = []
result = []
for i in range(1, N+1):
    data.append(i)
while len(data) > 0:
    if len(data) < K:
        
    else:
        num = data.pop(2)
        result.append(num)

print(result)