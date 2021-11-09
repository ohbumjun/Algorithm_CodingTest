# 주어진 숫자가 해당 범위 안에 있는지 확인하기
def in_range(n, start, end = 0):
    return start <= n <= end if end >= start else end <= n <= start

# examples
in_range(3, 2, 5)  # true
in_range(2, 4)  # true
in_range(1, 3, 5) # false