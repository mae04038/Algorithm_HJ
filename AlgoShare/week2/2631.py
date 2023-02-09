# LIS알고리즘 가장 긴 증가하는 부분 수열
# dp에 담긴 값: 현재 값까지 최장 길이 부분 수열은 무엇인가
N = int(input())
ans = 0
data = []
for _ in range(N):
    data.append(int(input()))
dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)
ans = N - max(dp)
print(ans)