def solution(triangle):
    answer = 0
    dp = [[0]*(len(triangle)) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle)): 
            if j > i:
                break
            if j == i:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            elif j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][0]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    answer = max(dp[-1])
    return answer