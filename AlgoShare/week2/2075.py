import heapq
q = []
N = int(input())
for _ in range(N):
    nums = map(int, input().split())
    for n in nums:
        if len(q) < N:
            heapq.heappush(q, n)
        else:
            if q[0] < n: # 최솟값이 n보다 작을 경우 n 큐에 넣기
                heapq.heappop(q)
                heapq.heappush(q, n)
print(q[0])


'''
메모리 초과 답안

N = int(input())
data = []
for _ in range(N):
    data.extend(map(int, input().split()))
data.sort(reverse=True)
print(data[N-1])
'''


