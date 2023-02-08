# 경우의 수: 3가지 + - ' '(공백)
import copy
def back_tracking(new_arr):
    if len(new_arr) == N-1:
        arr.append(copy.deepcopy(new_arr))
        return
    
    # 아스키코드 순대로 했을 때 공백이 우선순위
    new_arr.append(' ')
    back_tracking(new_arr)
    new_arr.pop()

    new_arr.append('+')
    back_tracking(new_arr)
    new_arr.pop()

    new_arr.append('-')
    back_tracking(new_arr)
    new_arr.pop()

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    back_tracking([])

    for op in arr:
        tmp = ""
        for n in range(1, N):
            tmp += str(n) + str(op[n-1])
        tmp += str(N)

        if eval(tmp.replace(" ", "")) == 0:
            print(tmp)
    
    print()
    


    