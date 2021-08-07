# https://programmers.co.kr/learn/courses/30/lessons/77486

# 첫번째 풀이 (시간초과) ---------------------------------
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    # 자기 이익 90% = 자기꺼
    # 자기 이익 10% = 추천인꺼
    # 원단위 절사
    # 10%가 1원 미만일 경우, 자기가 모두 가짐
    # 위의 과정은, 재귀적으로 일어난다.

    # dict(1_d) 안에 [배열]
    # 1_d 의 key = name
    # 배열 : 1) 추천인 name 2) 총 이익
    d = defaultdict(list)
    enroll_len = len(enroll)
    for i in range(enroll_len):
        d[enroll[i]] = [referral[i], 0]
    seller_len = len(seller)
    for i in range(seller_len):
        seller_p = seller[i]
        income = amount[i] * 100
        while True:
            # 금액 계산
            up_inc = int(income*0.1)
            my_inc = income - up_inc
            # 자기 이익 처리
            if up_inc < 1:
                my_inc = income
            d[seller_p][1] += my_inc
            # 추천인 이익 처리
            inv_p = d[seller_p][0]
            if inv_p == '-':
                break
            # 정보 update
            seller_p = inv_p
            income = up_inc
    res = []
    for i in range(enroll_len):
        res.append(d[enroll[i]][1])
    return res
