def solution(n, s):
    answer = []
    # 원소의 합이 s이면서 곱이 가장 크도록 - n 경우의수로 적어서 풀어보기
    if s//n == 0:
        return [-1]
    while n >= 1:
        answer.append(s//n)
        s -= s//n
        n -= 1

    return answer
