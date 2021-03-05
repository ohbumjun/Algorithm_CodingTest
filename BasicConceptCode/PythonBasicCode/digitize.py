# 숫자를 자릿수를 기준으로 분류해서 나누세요
def digitize(n) :
    return list(map(int, str(n)))

# 코드 분석
# 1) str(n) : 숫자를 문자열로 만들어준다
# 2) map(int, str(n)) : 문자열로 되어있는 각 자릿수를 정수로 바꿔준다( ex, "123" > 정수 1, 2, 3 각각으로 바꿔준다)
# 즉, 리스트의 모든 요소를 int를 사용해서 변환
# 3) list함수로 list 함수로 변환한다 

# examples
digitize(123) # [1,2,3]