from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1] # n발의 화살을 어떤 과녁 점수에 맞혀야 하는지
    
    max_gap = -1
    max_arrow = []
    gap = 0
    for cwr in combinations_with_replacement(range(11), n):
        
        info2 = [0]*11 # 라이언 과녁
        for i in cwr:
            info2[10-i] += 1 # 10-i 해줘야 info랑 순서가 맞음. cwr: 0점 1점 순이기 때문에
        
        apeach, lion = 0, 0 # 각각의 점수
        for idx in range(11):
            if info[idx] == info2[idx] == 0: # 둘다 0개일 때, 아무도 점수 획득 불가
                continue
            if info[idx] >= info2[idx]: # 어피치 개수가 더 많을 때
                apeach += 10 - idx
            else: # 라이언 개수가 더 많을 때
                lion += 10 - idx
                
        
        if lion > apeach : # 가장 낮은 점수를 많이 맞춘 걸로 업데이트 해줘야 함.
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = info2.copy()
        
    
    return answer