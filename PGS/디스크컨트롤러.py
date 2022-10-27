import heapq
def solution(jobs):
    answer = 0
    
    q = []
    now = 0 #현재시점
    start = -1 #이전에 완료한 일의 시작시간
    i = 0
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업 heap에 저장(나중에 소요시간이 적은걸 꺼낼것) 
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q, (job[1], job[0]))
        
        if len(q) > 0: #처리할 작업이 남아 있는 경우
            task = heapq.heappop(q)
            start = now
            now += task[0] # 총 소요시간 더해주기
            answer += now - task[1] # 요청시간부터 종료시간까지의 소요시간 계산
            i += 1
        else: #처리할 작업이 없는 경우
            now += 1 # 현재시점을 다음시간으로 넘어가기 위해 (요청시간이 연속적이지 않은 경우)
            
    
    return answer // len(jobs)