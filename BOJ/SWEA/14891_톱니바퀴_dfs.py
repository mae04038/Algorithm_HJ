gears = [list(map(int, input())) for _ in range(4)]
K = int(input())  # 명령어 개수


def rotate_right(gears):  # 리스트 회전하는 함수
    tmp = gears[7]
    for i in range(6, -1, -1):
        gears[i+1] = gears[i]
    gears[0] = tmp


def rotate_left(gears):
    tmp = gears[0]
    for i in range(7):
        gears[i] = gears[i+1]
    gears[7] = tmp


def dfs(num, d):
    global visited
    if not visited[num]:
        visited[num] = 1
        right = gears[num][2]  # 나중에 회전하기 때문에 미리 값 저장
        left = gears[num][6]
        if d == 1:
            rotate_right(gears[num])
        else:
            rotate_left(gears[num])

        if num-1 >= 0 and left != gears[num-1][2]:
            dfs(num-1, -d)  # 왼쪽 부분 계속 회전가능여부 확인
        if num+1 <= 3 and right != gears[num+1][6]:
            dfs(num+1, -d)  # 오른쪽 부분 계속 회전가능여부 확인


for _ in range(K):
    n, dir = map(int, input().split())
    visited = [False] * 4
    dfs(n-1, dir)

ans = 0
for i in range(4):
    if gears[i][0] == 1:
        # print(2**i)
        ans += 2**i
print(ans)
