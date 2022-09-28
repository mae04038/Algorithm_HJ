import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# dx = [0, 0, -1, 1] - 사용하면 메모리초과
# dy = [1, -1, 0, 0]

def dfs(x, y):
    global size_cnt

    # for i in range(4):
    #     nx = x + dx[i]
    #     ny = y + dy[i]
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if data[x][y] == 1:
        size_cnt += 1
        data[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False
    
             
max_size = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            size_cnt = 0
            dfs(i, j)
            max_size.append(size_cnt)
            
if len(max_size) == 0:
    print(len(max_size))
    print(0)
else:
    print(len(max_size))
    print(max(max_size))