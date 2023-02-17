import math
def solution(str1, str2):
    answer = 0
    
    str1 = str1.upper()
    str2 = str2.upper()
    list1 = []
    list2 = []
    for i in range(len(str1)-1):
        tmp = str1[i]+str1[i+1]
        if tmp.isalpha():
            list1.append(tmp)
    for i in range(len(str2)-1):
        tmp = str2[i]+str2[i+1]
        if tmp.isalpha():
            list2.append(tmp)
    
    # print(list1)
    # print(list2)
    min_cnt = []
    for word in set(list1+list2):
        cnt1 = list1.count(word)
        cnt2 = list2.count(word)
        m = min(cnt1, cnt2)
        min_cnt.append(m)
    max_cnt = len(list1) + len(list2) - sum(min_cnt)
    
    if sum(min_cnt) == 0 and max_cnt == 0: # 둘 다 공집합일 때
        answer = 1*65536
    elif sum(min_cnt) == 0 and max_cnt != 0: # 교집합이 없는 경우
        answer = 0
    else: # 교집합 존재하는 경우
        answer = sum(min_cnt)/max_cnt * 65536
    answer = math.trunc(answer)
    
    return answer