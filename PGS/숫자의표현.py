def solution(n):
    answer = 1  # 자기자신은 미리 더해주기

    res = 0
    for i in range(1, n):
        for j in range(i, n):
            res += j
            if res > n:
                break
            elif res == n:
                answer += 1
                break
            else:
                continue
        if res >= n:
            res = 0

    return answer
