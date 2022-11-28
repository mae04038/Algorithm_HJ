from collections import Counter

T = int(input()) #테케
while T != 0:
    T -= 1
    W = input() # 문자열
    K = int(input())

    for i in range(len(W)):
        words = W[:i+1]
        count = Counter(words)
        target = ''
        if K in count.values():
            target = 


