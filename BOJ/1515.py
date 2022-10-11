'''
1 ~ N까지 수를 차례대로 쓸 때, 최솟값 N구하기
'''
tmp = input()
i = 0 # 최소숫자

while True:
    i += 1 # 1부터 탐색
    num = str(i)
    while len(num) > 0 and len(tmp) > 0:
        if num[0] == tmp[0]:
            tmp = tmp[1:]
        num = num[1:] # num이 10 이상인 경우 해당
        
    if tmp == '':
        print(i)
        break
