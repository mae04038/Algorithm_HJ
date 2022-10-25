def solution(genres, plays): # 장르 별로 가장 많이 재생된 노래 최대 2개씩 수록
    answer = []
    
    mostGenre = {}
    playlist = {}
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in mostGenre.keys():
            mostGenre[g] = p
            playlist[g] = [(idx, p)]
        else:
            mostGenre[g] += p
            playlist[g].append((idx, p))
    print(mostGenre)
    print(playlist)
    
    sorted_genres = sorted(mostGenre.items(), key=lambda x:x[1], reverse=True)
    
    for k, v in sorted_genres:
        sorted_play = sorted(playlist[k], key=lambda x:x[1], reverse=True)
        for i, p in sorted_play[:2]:
            answer.append(i)
    
    
    return answer

'''
정확성 20

def solution(genres, plays): # 장르 별로 가장 많이 재생된 노래 최대 2개씩 수록
    answer = []
    
    genre = {}
    play = {}
    idx = 0
    for g, p in zip(genres, plays):
        
        if g not in genre.keys():
            genre[g] = p
            play[g] = []
            play[g].append((idx, p))
        else:
            genre[g] += p
            play[g].append((idx, p))
        idx += 1
    print(genre)
    print(play)
    
    sorted_genre = sorted(genre.items(), reverse=True)
    print(sorted_genre)
    
    for g_name in sorted_genre:
        sorted_play = sorted(play[g_name[0]], key=lambda x:x[1], reverse=True)
        print(sorted_play)
        if len(sorted_play) == 1:
            answer.append(sorted_play[0][0])
        elif len(sorted_play) >= 2:
            for k in range(2):
                answer.append(sorted_play[k][0])
    
    return answer
'''