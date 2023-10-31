# https://programmers.co.kr/learn/courses/30/lessons/42577

# 1.이중 for문 : 시간 초과
def solution(phone_book):
    len_phone_book = len(phone_book)
    answer = True
    tup_arr = []
    # 배열을 돌면서, 길이와 문자열 tuple 형식으로 저장한다
    for phone in phone_book:
        tup_arr.append((len(phone), phone))
    tup_arr.sort()

    for i in range(len_phone_book):
        origin_num = tup_arr[i][1]
        for j in range(i, len_phone_book):
            if i == j:
                continue
            comp_num = tup_arr[j][1]
            if len(comp_num) < len(origin_num):
                continue
            if comp_num[:len(origin_num)] == origin_num:
                return False
    return answer

# sort를 활용한 간단한 방법


def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer


'''
문자열의 특성을 잘 활용한 코드이다
sort()를 하게 되면
문자열 내의 number 순으로 오름차순 정렬된다.
즉, 현재 보는 phone_num이 i번째라면
해당 num이 다른 num의 접두어이려면,
반드시 다음 것이 접두어이어야 한다 
왜냐하면, 다음 것의 접두어도 아닌데, 그 이후의 단어에 대해서 접두어 일리 없기 때문이다 



'''
