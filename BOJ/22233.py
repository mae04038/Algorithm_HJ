N, M = map(int, input().split()) # N: 키워드 개수, M:블로그에 쓴 글의 개수
keywords = {}

for _ in range(N):
    keywords[input()] = 1

# print(keywords)
cnt = N
for _ in range(M):
    
    blogs = input().split(",")
    for word in blogs:
        if word in keywords.keys():
            if keywords[word] == 1:
                keywords[word] -= 1
                cnt -= 1
    
    blogs.clear()
    print(cnt)
    
    