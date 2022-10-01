N = int(input())
alphabets = []
data = {}
alpha_num_list = []

for _ in range(N):
    alphabets.append(input())

for k in range(N):
    word = alphabets[k]
    visited = [False] * len(word)
    match = ''
    for i in range(len(word)):
        match = '1'
        for j in range(i+1, len(word)):
            if word[i] == word[j] and not visited: #같은 알파벳이 있으면
                visited[j] = True
                match = match + '1'
            else:
                match = match + '0'
        if word[i] not in data.keys() :
            data[word[i]] = int(match)
        else:
            data[word[i]] += int(match)
        # print(match)

# print(data)        
answer = 0
alpha_num_list = sorted(data.values(), reverse=True)
# print(alpha_num_list)
for i in range(len(alpha_num_list)):
    answer += (9-i)*alpha_num_list[i]

print(answer)
