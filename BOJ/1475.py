N = int(input())
data = {'0':0, '1':0, '2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,}
room = str(N)
for i in range(len(room)):
    if room[i] in ['6', '9']:
        data['6'] += 1
    else:
        data[room[i]] += 1
if data['6'] % 2 == 0:
    data['6'] //= 2
else:
    data['6'] = data['6']//2 + 1
print(max(data.values()))

# for i in range(len(room)):
#     if room[i] in data.keys():
#         data[room[i]] += 1
#     else:
#         data[room[i]] = 1
# sortedData = sorted(data.items(), key=lambda x:x[1])
# # print(sortedData)
# if sortedData[-1][1] == 1:
#     print(1)
# elif sortedData[-1][0] == '9' or sortedData[-1][0] == '6': # 6혹은 9가 최빈수일때
#     six_nine = 0
#     if '9' in data.keys():
#         six_nine += data['9']
#     if '6' in data.keys():
#         six_nine += data['6']
#     answer = math.ceil(six_nine / 2)
#     print(answer)
# else:
#     print(sortedData[-1][1])