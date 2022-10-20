'''
테스트케이스 1, 2 통과못함 (정확성 50)
'''
def dfs(now, air, answer):
    if now not in air.keys():
        return
    if len(air[now]) == 0:
        print("돌아가기")
        return
    sortAir = sorted(air[now])
    
    for loc in sortAir:
        print(loc)
        answer.append(loc)
        air[now] = sortAir[1:]
        print(air)
        dfs(loc, air, answer)
        break
          
def solution(tickets):
    answer = []
    
    air = {}
    
    for tk in tickets:
        if tk[0] not in air.keys():
            air[tk[0]] = []
            air[tk[0]].append(tk[1])
        else:
            air[tk[0]].append(tk[1])
            
    # print(air) #공항 경로 연결정보
    
    answer.append("ICN")
    dfs("ICN", air, answer)
    
    
    
    return answer