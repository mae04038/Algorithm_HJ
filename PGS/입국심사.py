def solution(n, times):
    answer = 0

    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        cnt = 0

        for time in times:
            cnt += mid // time
            if cnt >= n: #모든 심사관을 거치지 않아도 n명 다 검사 가능하면 탈출
                break
        if cnt >= n:
            answer = mid
            right = mid - 1
        elif cnt < n:
            left = mid + 1

    '''
    정확성 33.3

    result = []
    # 모든 사람이 심사를 받는 데 걸리는 시간을 최소로
    for i in range(1, n+1):
        for time in times:
            result.append(time*i)
    result.sort()
    answer = result[n-1]
    '''

    return answer
