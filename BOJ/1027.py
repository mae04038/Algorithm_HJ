'''
기울기 문제
-  오른쪽: 이전에 있는 빌딩들보다 기울기가 크면 볼 수 있는 건물
- 왼쪽 : 이전에 있는 빌딩들보다 기울기가 작아야 볼 수 있음.
'''
N = int(input()) # 빌딩의 수
data = list(map(int, input().split())) 
buildings = [0] * N # i-1번째 빌딩이 볼 수 있는 빌딩의 수

slope = [[0] * N for _ in range(N)] #slope[i][j] : 빌딩 i 와 j 사이의 기울기
for i in range(N):
    for j in range(N):
        if i == j: continue
        slope[i][j] = (data[i] - data[j]) / (i - j)        


for i in range(N):
    # print("%d 번째 빌딩" %i)
    
    #왼쪽 볼 수 있는 빌딩수
    min_slope = float('INF')
    for L in range(i-1, -1, -1):
        if L == -1 : break
        if slope[L][i] < min_slope:
            buildings[i] += 1
            min_slope = slope[L][i]

    #오른쪽 볼 수 잇는 빌딩수
    max_slope = -float('INF')
    for R in range(i+1, N):
        if R == N: break # index에러 해결
        if slope[i][R] > max_slope:
            buildings[i] += 1
            max_slope = slope[i][R]

    # print(buildings)
print(max(buildings))
