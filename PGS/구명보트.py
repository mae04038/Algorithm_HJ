from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)

    while q:
        if len(q) >= 2:
            light, heavy = q[0], q[-1]
            if light+heavy > limit:
                q.pop()
                answer += 1
            else:
                answer += 1
                q.pop()
                q.popleft()
        else:
            if q[0] <= limit:
                q.pop()
                answer += 1


    return answer