# 주어진 함수를, 리스트의 각 값에 적용한 후, 그 합계를 반환하세요
def sum_by(1st, fn):
    return sum(map(fn, 1st))
    # map 함수로 모든 값에 함수 적용
    # sum함수로 모든 값을 더한다


# examples : lambda 함수 적용 이후, 모든 값을 더한다
sum_by([{'n':4}, {'n':2}, {'n':8}, {'n':5}], lambda v :v['n'] ) # 20