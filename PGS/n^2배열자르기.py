'''
시간초과 해결 -> data 다 만들지 않고 해당 위치의 값만 바로바로 구해주기
'''
def solution(n, left, right):
    answer = []
        
    for k in range(left, right+1):
        answer.append(max(k//n, k%n)+1)

    
    return answer