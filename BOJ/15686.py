'''
(r, c) r행 c열
빈칸: 0
치킨집: 2
집: 1
치킨거리 - 집과 가장 가까운 치킨집 사이의 거리, 집을 기준으로 정해짐
도시의 치킨거리 - 모든 집의 치킨거리의 합
도시의 치킨거리가 가장 작게 될때 도시의 치킨거리의 최솟값 출력
<생각1>
조합 사용 - 치킨집 중 M개 고르는 경우 중 도시치킨거리가 최소일 때 출력
'''
from itertools import combinations

N, M = map(int, input().split()) # M : 남겨둘 치킨집 개수
city = []
chicken = [] # 치킨집의 좌표
home = [] # 집의 좌표

for i in range(N):
    city.append((list(map(int, input().split()))))
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            home.append((i, j))


# print(list(combinations(chicken, M)))
result = []
for tmp in combinations(chicken, M):
    # print(tmp)
    chicken_length = 0
    res = 0
    for house in home:
        min_length = 1000
        for chick in tmp:
            chicken_length = abs(chick[0] - house[0])+abs(chick[1] - house[1])
            min_length = min(min_length, chicken_length)
        # print("도시의 치킨거리",min_length)
        res += min_length
    # print("해당 조합 치킨거리", res)
    result.append(res)

print(min(result))