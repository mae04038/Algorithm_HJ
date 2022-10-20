N = int(input())
data = list(map(int, input().split()))
tmp = sorted(set(data))
print(tmp)
result = {tmp[i]: i for i in range(len(tmp))}
print(result)

for num in data:
    print(result[num], end=" ")