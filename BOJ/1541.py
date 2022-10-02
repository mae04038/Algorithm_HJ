''' 
'-'가 있으면 그 뒤로 '-' 기준split
'''
data = input().split('-')
result = []
for num in data:
    cnt = 0
    if '+' in num:
        num = num.split('+')
        for n in num: cnt += int(n)
    else:
        result.append(int(num))
    result.append(cnt)
answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]
print(answer)






