import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 회의실 수, 예약된 수
rooms = {}

for _ in range(N):
    room = input().rstrip()
    rooms[room] = [[i, i+1] for i in range(9, 18)]

for _ in range(M):
    name, start, finish = map(str, input().split())
    for i in range(int(start), int(finish)):
        rooms[name].remove([i, i+1])



for roomName in sorted(rooms.keys()):
    print("Room %s:"%roomName)
    if len(rooms[roomName]) == 0:
        print("Not available")
    else:
        tmp = []
        answer = []
        for i in range(len(rooms[roomName])):
            if i == len(rooms[roomName]) == 1:
                tmp.append(rooms[roomName][i])

            if i ==  len(rooms[roomName])-1:
                tmp.append(rooms[roomName][i])
            elif 0 <= i < len(rooms[roomName])-1:
                if rooms[roomName][i][1] == rooms[roomName][i+1][0]:
                    tmp.append(rooms[roomName][i])
                else:
                    tmp.append(rooms[roomName][i])
                    answer.append([tmp[0][0], tmp[-1][1]])
                    tmp = []

        if tmp == []:
            pass
        else:
            answer.append([tmp[0][0], tmp[-1][1]])
        

        print(len(answer), "available:")   
        for i in range(len(answer)):
            if answer[i][0] == 9:
                answer[i][0] = "09"
                print(answer[i][0]+"-"+str(answer[i][1]))
            else:
                print(str(answer[i][0])+"-"+str(answer[i][1]))
            
            
    if roomName == sorted(rooms.keys())[-1]:
        break
    else:
        print("-----")




