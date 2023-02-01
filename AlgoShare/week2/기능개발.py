from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    
    q = deque()
    
    for p, s in zip(progresses, speeds):
        q.append(math.ceil((100-p)/s))
    
    cnt = 1
    while q:
        if cnt > 1: # 배포개수가 여러개일 때 큐에서 배포된 것 빼주기 (동시에 cnt도 감소시키기)
            now = q.popleft()
            cnt -= 1
            continue
            
        now = q.popleft()
        for pg in q:
            if now >= pg:
                cnt += 1
            else:
                break
        answer.append(cnt)
    
    return answer