# 두 리스트에 모두 존재하는 공통값을 반환하기
def intersection(a,b):
    _a, _b = set(a), set(b)
    return list(_a & _b) # set연산은 교집합 연산이 가능하다 > 그 다음 list 함수를 통해 list 자료형으로 변환한다

# examples
intersection([1,2,3], [2,3,4])