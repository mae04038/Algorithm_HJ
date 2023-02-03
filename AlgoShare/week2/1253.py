N = int(input())
data = list(map(int, input().split()))
answer = 0

data.sort()

for i in range(N):
    tmp = data[:i] + data[i+1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == data[i]:
            answer += 1
            break
        if t < data[i]:
            left += 1
        else:
            right -= 1

print(answer)
    
