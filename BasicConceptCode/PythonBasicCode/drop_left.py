# 왼쪽에서부터 n개의 요소가 제거된 list를 만들어라
def drop(a, n = 1):
    return a[n:]
    # n값이 없을때는 왼쪽에서 한개만 제거되는 default원리를 적용한다

# examples
drop([1,2,3]) # [2,3]
