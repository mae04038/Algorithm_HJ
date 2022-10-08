'''10일 연속으로 일치할 경우에 맞춰서 회원가입'''
from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for w, n in zip(want, number):
        dic[w] = n
        
    for start in range(len(discount)-9):
        # print("start", start)
        counter = Counter(discount[start:start+10])
        # print(counter)
        if dic == counter:
            answer += 1

    return answer