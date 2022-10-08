from collections import deque

def bfs(wire, data, n, visited):
    cnt = 1
    q = deque()
    q.append(wire)
    visited[wire] = True
    while q:
        node = q.popleft()
        for nd in data[node]:
            if not visited[nd]:
                visited[nd] = True
                q.append(nd)
                cnt += 1
    return cnt

def solution(n, wires):
    answer = 101
    tmp = 0
    data = [[] for _ in range(n+1)]
    
    for wire in wires:
        data[wire[0]].append(wire[1])
        data[wire[1]].append(wire[0])
    
    for wire in wires: # 하나씩 끊어보고 한쪽 bfs
        visited = [False] * (n+1)
        visited[wire[0]] = True
        tmp = bfs(wire[1], data, n, visited) #한쪽 트리만 탐색하면 됨.
        print(tmp)
        answer = min(answer, abs((n-tmp)-tmp))
        
    
    return answer