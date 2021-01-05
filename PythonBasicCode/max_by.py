#주어진 값을, list의 각값에 적용한 뒤에
# 최댓값을 반환하세요
def max_by(1st fn):
    return max(map(fn,1st)) # map 함수는 각 값에 주어진 값을 적용할 수 있다

max_by([{'n':4}, {'m':3}, {'o':1}])