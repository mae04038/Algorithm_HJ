from collections import deque

def solution(begin, target, words):
    answer = 51
    
    if target not in words: return 0
    
    q = deque()
    q.append((begin, 0)) # 시작단어랑 cnt
    visited = [False] * len(words)
    while q:
        now, cnt = q.popleft()
        
        if now == target:
            answer = min(answer, cnt)
            
        for i in range(len(words)):
            unmatch = 0
            for j in range(len(begin)):
                if words[i][j] != now[j]: unmatch += 1
            if unmatch == 1 and not visited[i]:
                q.append((words[i], cnt + 1))
                visited[i] = True
        print(q)
    
    return answer
'''
정확성 60/100
result = []
def dfs(cnt, now, words, target):
    
    if now == target:
        result.append(cnt)
        return 
    for word in words:
        
        if word[0] == now[0] and word[1] == now[1] and word[2] != now[2]:
            words.remove(word)
            dfs(cnt+1, word, words, target)
            words.append(word)
        if word[0] == now[0] and word[1] != now[1] and word[2] == now[2]:
            words.remove(word)
            dfs(cnt+1, word, words, target)
            words.append(word)
        if word[0] != now[0] and word[1] == now[1] and word[2] == now[2]:
            words.remove(word)
            dfs(cnt+1, word, words, target)
            words.append(word)
    return
        

def solution(begin, target, words):
    answer = 0
    
    if target not in words: return 0
    
    for word in words:
        if word[0] == begin[0] and word[1] == begin[1] and word[2] != begin[2]:
            # print("확인1")
            words.remove(word)
            dfs(1, word, words, target)
        if word[0] == begin[0] and word[1] != begin[1] and word[2] == begin[2]:
            # print("확인2")
            words.remove(word)
            print(words)
            dfs(1, word, words, target)
        if word[0] != begin[0] and word[1] == begin[1] and word[2] == begin[2]:
            # print("확인3")
            words.remove(word)
            dfs(1, word, words, target)
            
    print(result)
    answer = min(result)
    
    return answer

'''