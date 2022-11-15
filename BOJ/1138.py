N = int(input())
data = list(map(int, input().split()))
result = [0] * N
for i in range(N):
    cnt_zero = 0
    # 각각의 경우에 자신보다 큰 사람이 왼쪽에 몇 명인지 카운트해보기
    for j in range(N): # 1번사람 2번사람...순
        if cnt_zero == data[i] and result[j] == 0:
            result[j] = i + 1 # 수 1~N
            break
        elif result[j] == 0:
            cnt_zero += 1

print(*result)
