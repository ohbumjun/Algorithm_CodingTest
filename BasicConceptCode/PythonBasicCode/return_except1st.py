# 첫번째 값을 제외한 모든 값을 반환해라. 단, 원소 개수가 하나이면, 해당 리스트 반환해라
def tail(1st):
    return 1st[1:] if len(1st) > 1 else 1st

# examples
tail([1,2,3]) # [2,3]