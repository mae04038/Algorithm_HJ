def solution(operations):
    answer = []
    q = []
    for op in operations:
        opt, num = op.split(" ")
        # print(opt, num)
        
        if opt == "I":
            q.append(int(num))
        elif opt == "D" and num == "-1" and len(q) >= 1: # 최솟값 삭제
            q.remove(min(q))
        elif opt == "D" and num == "1" and len(q) >= 1:
            q.remove(max(q))
    
    if len(q) == 0:
        answer = [0, 0]
    else:
        answer = [max(q), min(q)]
    return answer