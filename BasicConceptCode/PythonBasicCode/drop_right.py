# slice기법
def drop_right(a, n=1):
    return a[:-n] # -를 사용하면, 배열에서 뒤에서부터 접근할 수 있다

# examples
drop_right([1,2,3]) # [1,2]