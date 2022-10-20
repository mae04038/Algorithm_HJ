def solution(tickets):
    path = []

    air = {}
    for tk in tickets:
        if tk[0] not in air.keys():
            air[tk[0]] = []
            air[tk[0]].append(tk[1])
        else:
            air[tk[0]].append(tk[1])

    for a in air.keys():
        air[a].sort(reverse=True) #역순정렬
    print(air)

    stack = ["ICN"]
    while stack:
        print("스택", stack)
        now = stack.pop()
        if now not in air.keys() or not air[now]: #now를 시작점으로 하는 경로가 없거나 now연결된 도시가 없을 때
            path.append(now) # path에 넣어주기
            print(path)
        else:
            # 연결된 경로가 있으면 다시 스택에 넣어주고, 연결된 곳 넣어주기
            stack.append(now)
            stack.append(air[now].pop()) # 연결된 곳 스택에 넣어줌과 동시에 딕셔너리에서는 제거

    return path[::-1]
