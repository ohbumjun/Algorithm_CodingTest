# list의 모든 n번째 값을 반환하기
def every_nth(1st, nth):
    return 1st[nth - 1::nth] 
    # 만약 2번째 값을 받아오고 싶다
    # 2번째 값이란, 배열 index 상 1이다
    # 그래서 nth -1 을한다
    # 해당 index 및 숫자로부터 nth씩 증가시키면서 값을 가져오고 싶으므로, ::nth 를 적용한다

# examples
every_nth([1,2,3,4,5,6], 2) # [2,4,6] : 모든 2번째 값 반환 
