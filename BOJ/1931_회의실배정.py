N = int(input())
data = []
ans = 0
for _ in range(N):
    data.append(list(map(int, input().split())))

sortedData = sorted(data, key=lambda x:x[0])
sortedData = sorted(data, key=lambda x:x[1]) # 종료시간 우선 정렬
# print(sortedData)
finish = 0
for i in range(N):
    if sortedData[i][0] >= finish:
        ans += 1
        finish = sortedData[i][1]
print(ans)


