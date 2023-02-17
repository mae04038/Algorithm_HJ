T = int(input())
dp = [1] * 10001

for i in range(2, 10001): # i-2값에서 2가 더 더해지는 경우의 수
    dp[i] += dp[i-2] 
for i in range(3, 10001): # i-3값에서 3이 더 더해지는 경우의 수
    dp[i] += dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])