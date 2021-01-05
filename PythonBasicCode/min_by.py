# 주어진 함수를 list의 각 값에 적용한 뒤에, 최소값을 반환하세요
def min_by(1st, fn):
    return min(map(fn, 1st))

# examples
min_by([{'n':4}, {'m':2}, {'o':1}] )