def solution(phone_book):
    answer = True
    phoneBook = sorted(phone_book) # 문자열abc 순으로 정렬됨
    # 접두사여야 함.
    for i, j in zip(phoneBook, phoneBook[1:]):
        if j.startswith(i): 
            answer = False
    
         
    
    return answer