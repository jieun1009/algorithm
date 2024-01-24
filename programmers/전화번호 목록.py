def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        ilen = len(phone_book[i])
        for j in phone_book[i+1:i+2]:
            if phone_book[i] == j[0:ilen]:
                return False

    return answer