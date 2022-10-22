import sys
input = sys.stdin.readline
N = int(input())
data = [int(input().rstrip()) for _ in range(N)]
answer = 0

# print(data)

positive = []
negative = []
pos_res = 0
neg_res = 0

for i in data:
    if i > 1: positive.append(i)
    elif i == 1: answer += 1
    else: negative.append(i)
positive.sort(reverse=True) #내림차순
negative.sort() #오름차순

if len(positive)%2 == 0:
    for i in range(0, len(positive), 2):
        pos_res += positive[i]*positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        pos_res += positive[i]*positive[i+1]
    pos_res += positive[-1]

if len(negative)%2 == 0:
    for i in range(0, len(negative), 2):
        neg_res += negative[i]*negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        neg_res += negative[i]*negative[i+1]
    neg_res += negative[-1]

answer += neg_res + pos_res


print(answer)

