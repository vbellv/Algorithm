def solution(phone_book):
    
    phone_book.sort()
    
    for idx in range(len(phone_book)-1):
        for i in range(idx+1, len(phone_book)):
            if phone_book[idx] == phone_book[i][:len(phone_book[idx])]:
                return False
            break
    return True