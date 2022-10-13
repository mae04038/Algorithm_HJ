'''
참고 : https://www.youtube.com/watch?v=z4wKvYdd6wM
같은 행, 열, 대각선에는 다른 퀸을 놓을 수 없음
기본가정 : 퀸은 항상 다른 행에 위치시킴 -> 같은 행에 놓인건지는 확인할필요 X
dfs - 백트래킹
pypy 제출
'''

# 같은 열이나 같은 대각선에 있는지 확인
def isPromising(node): # node는 열, 
    for i in range(node): # 현재 퀸 위치의 윗부분만 체크하면 됨.
        if abs(col[i] - col[node]) == abs(i - node) or col[i] == col[node]:
            return False
    return True    

def dfs(depth):
    global answer

    if depth == N:
        answer += 1 # 솔루션 찾음 -> answer + 1해주기
    else:
        # 각 행에 퀸 놓기
        for i in range(N):
            if visited[i]:
                continue

            col[depth] = i # depth행의 퀸의 위치는 i열
            if isPromising(depth): # 유망하면 dfs
                visited[i] = True
                dfs(depth + 1)
                visited[i] = False
            

N = int(input())
col = [-1] * N # col[i] : i번째 행에 있는 퀸의 열 위치
visited = [False] * N # 시간초과해결 - 방문여부 체크해주기
answer = 0

dfs(0)
print(answer)




