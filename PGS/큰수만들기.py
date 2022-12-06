def solution(number, k):
    stack = []
    for n in number:
        # 스택의 마지막 값이 push할 값보다 작으면 크거나 같은 값이 나올 때까지 pop
        while stack and stack[-1] < n and k > 0:
            k -= 1
            # print("제거", stack[-1])
            stack.pop()
        stack.append(n)
        # print(stack,"스택")

    if k != 0: #테케 12 해결
        stack = stack[:-k]
        
    return ''.join(stack)

'''
정확성 33.3
from itertools import combinations
def solution(number, k):
    answer = ''
    results = []
    for combi in combinations(number, len(number)-k):
        nums = ''.join(combi)
        results.append(int(nums))
    answer = str(max(results))
    
    return answer
'''