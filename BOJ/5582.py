# 참고 : https://dailylifeofdeveloper.tistory.com/114
import sys
input = sys.stdin.readline
word1 = input().rstrip()
word2 = input().rstrip()

answer = 0

dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

for i in range(1, len(word1)+1):
    for j in range(1, len(word2)+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > answer:
                answer = dp[i][j]

print(answer)        
# print(max(map(max, dp)) # 각 array에서 max값만 추출

'''
시간초과

import itertools
import sys
input = sys.stdin.readline

answer = -1
word1 = input().rstrip()
word2 = input().rstrip()

big, small = '', ''
if len(word1)>=len(word2):
    big = word1
    small = word2
else:
    big = word2
    small = word1

# for combi in itertools.combinations(small, 7):
#     words = ''.join(combi)
#     print(words)

for i in range(len(small), -1, -1):
    for combi in itertools.combinations(small, i):
        if answer >= 0:
            break
        words = ''.join(combi)
        if words in big:
            print(i)
            answer = i
            
'''

        
