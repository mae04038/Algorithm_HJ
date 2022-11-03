N = int(input())
data = [[] for _ in range(N+1)]

for i in range(N):
    num = int(input())
    data[num].append(i+1)

answer = set()

for i in range(1, N+1):
    visited = [False] * (N+1)
    stack = [i]
    visited[i] = True

    while stack:
        print("스택", stack)
        now = stack.pop()

        for nd in data[now]:
            if not visited[nd]:
                stack.append(nd)
                visited[nd] = True
            elif visited[nd] and nd == i:
                answer.add(nd) # 사이클 생성됨
                print(answer)
                
answer = list(answer)
answer.sort()
print(len(answer))
for ans in answer:
    print(ans)




'''
### 시간초과

import itertools
N = int(input())
data = {}
answer = []
same = 0
for idx in range(1, N+1):
    data[idx] = int(input())
for i in range(N, -1, -1):
    for combi in itertools.combinations(data, i):
        if same == 1:
            break

        res = list(combi)
        check = []
        for j in res:
            check.append(data[j])
        # print(check)
        # print("정수", res)
        check.sort()
        if check == res:
            # print("같음")
            answer = res
            # print(answer)
            same = 1
        
print(len(answer))
for ans in answer:
    print(ans)
'''
