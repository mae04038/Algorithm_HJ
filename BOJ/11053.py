N = int(input()) # 수열 크기, 길이
data = list(map(int, input().split()))

# dp: 자신을 포함하여 만들 수 있는 부분수열의 개수 저장
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
