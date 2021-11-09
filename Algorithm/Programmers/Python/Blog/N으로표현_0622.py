# https://programmers.co.kr/learn/courses/30/lessons/42895
# 참고 : https://gurumee92.tistory.com/164

def solution(N, number):
    answer = 0
    # set 생성 하기
    s = [set() for x in range(8)]
    for i in range(8):
        s[i].add(int((i+1)*str(N)))
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer

    '''
    1) 숫자를 n개 써서 만드는 경우의 수 
    = 숫자를 n개 이어붙이기
    = (1개 써서 만드는 경우수) U (n-1 개 써서 만드는 경우수)
    = (2개 써서 만드는 경우수) U (n-2 개 써서 만드는 경우수)
    = (3개 써서 만드는 경우수) U (n-3 개 써서 만드는 경우수)
    ...
    
    여기서 U는, 사칙연산을 말하는 것
    
    2) 중복되는 숫자가 있을 수 있다
    - set을 활용한다 
    
    3) 8번까지만 반복 가능하다
    즉, 숫자를 1개,2개....8개 사용하여 만드는 숫자들을 조사한 이후
    그 중에서 number 가 존재하는지 확인하면 된다 
    
    
    
    '''
    return answer
