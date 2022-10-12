'''
백트래킹 (dfs)
숫자 순서는 유지, 그 사이에 연산자 넣어주며 식 바꿔주기
첫번째 숫자에 첫 연산자를 넣고 dfs 돌린 후,
다시 백트래킹을 통해 원래 상태로 되돌리기
두번째 연산자 넣고 dfs 돌린 후, 다시 백트래킹으로 원래 상태로 되돌리기
-> 반복하면서 모든 경우의 수 탐색
'''
N = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maximum = -1e9
minimum = 1e9

def dfs(depth, total):
    global maximum, minimum, add, sub, mul, div

    if depth == N:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
    else:
        if add > 0:
            add -= 1
            dfs(depth + 1, total + data[depth])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(depth + 1, total - data[depth])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(depth + 1, total * data[depth])
            mul += 1
        if div > 0:
            div -= 1
            dfs(depth + 1, int(total/data[depth]))
            div += 1


dfs(1, data[0])

print(maximum)
print(minimum)
