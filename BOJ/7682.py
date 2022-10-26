def isWin(case, type):
    if case[0][0] == case[0][1] == case[0][2] == type :
        return True
    if case[1][0] == case[1][1] == case[1][2] == type:
        return True
    if case[2][0] == case[2][1] == case[2][2] == type:
        return True
    if case[0][0] == case[1][0] == case[2][0] == type:
        return True
    if case [0][1] == case[1][1] == case[2][1] == type:
        return True
    if case[0][2] == case[1][2] == case[2][2] == type:
        return True
    if case[0][0] == case[1][1] == case[2][2] == type:
        return True
    if case [0][2] == case[1][1] == case[2][0] == type:
        return True
    return False

while True:
    data = input().rstrip()
    if data == 'end': break
    else:
        case = []
        for i in range(0, 9, 3):
            case.append(data[i:i+3])

        cntX = data.count('X')
        cntO = data.count('O')
        empty = data.count('.')

        if cntX > cntO+1:
            print('invalid')
            continue
        if cntO > cntX:
            print('invalid')
            continue

        if cntO == cntX : # O가 이기는 경우
            if isWin(case, 'O') and not isWin(case, 'X'):
                print('valid')
                continue
        if cntX == cntO+1 : # X가 이기는 경우 - X가 이겨야 함.
            if isWin(case, 'X') and not isWin(case, 'O') :
                print('valid')
                continue
        if cntX == 5 and cntO == 4: # 무승부인 경우 O가 이기면 안됨
            if not isWin(case, 'O'):
                print('valid')
                continue
        
        print('invalid')