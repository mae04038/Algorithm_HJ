import heapq

N = int(input())
hq = []
answer = 0
for _ in range(N): heapq.heappush(hq, int(input()))

while len(hq) != 1:
    result = 0
    result += heapq.heappop(hq)  
    result += heapq.heappop(hq)
    answer += result
    heapq.heappush(hq, result)
print(answer)  
    


''' 시간초과 
import sys
input = sys.stdin.readline
N = int(input())
data = []
answer = 0
for _ in range(N): data.append(int(input()))

if N > 2:
    while len(data) != 1:
        data.sort()
        answer += data[0] + data[1]
        data.append(data[0] + data[1])
        data = data[2:]
        # print("answer", answer)
        # print(data)
    # answer += data[0]

else:
    answer = sum(data)

print(answer)
'''

