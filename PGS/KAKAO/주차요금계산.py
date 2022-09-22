import math
def solution(fees, records):
    answer = []
    cars = {}
    car_num = {}
    for record in records:
        info = record.split(" ")
        if info[1] not in cars.keys():
            cars[info[1]] = []
            cars[info[1]].append(info[0])
            car_num[info[1]] = 0
        else:
            cars[info[1]].append(info[0])
    # print(cars)

    for i in cars: # 각각 차의 누적시간 확인 가능 -> 계산
        # print(cars[i])
        # print(cars[i][0])
        total = 0 #누적시간
        cost = 0 # 요금
        # if len(cars[i])%2 == 0: #출차기록 확인 가능 경우
        for j in range(0, len(cars[i]),2):
            h, m = cars[i][j].split(":")
            if j == len(cars[i])-1:
                hh, mm = "23:59".split(":")
            else:
                hh, mm = cars[i][j+1].split(":")
            # total += 60 * (int(hh)-int(h))
            if int(mm) > int(m):
                total += 60 * (int(hh)-int(h))
                total += int(mm) - int(m)
            else:
                if int(hh) - int(h) != 1:
                    total += 60 * (int(hh)-int(h)-1)
                total += int(mm)+60 - int(m)

        # print(total)
        if total > fees[0]:
            cost = fees[1] + math.ceil((total - fees[0])/fees[2])*fees[3]
        else:
            cost = fees[1]
        # print("비용", cost)
        car_num[i] = cost

    # print(car_num)
    sortedCar = sorted(car_num.items())
    print(sortedCar)
    for i in range(len(sortedCar)):
        answer.append(sortedCar[i][1])

    return answer