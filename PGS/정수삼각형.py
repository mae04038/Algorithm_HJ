def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]

    dp[0][0] = triangle[0][0]

    for col in range(1, n):
        for row in range(len(triangle[col])):
            if row == 0:
                dp[col][row] = dp[col-1][0] + triangle[col][row]
            elif col == row:
                dp[col][row] = dp[col-1][row-1] + triangle[col][row]
            else:
                dp[col][row] = max(dp[col-1][row-1]+triangle[col][row], dp[col-1][row]+triangle[col][row])



    return max(dp[-1])