# 앞에서부터 n개의 값을 가져와라 : slicing 방법 사용하기
def take(itr, n = 1 ):
    return itr[:n]

# examples
take([1,2,3], 5)  # [1,2,3]
take([1,2,3],0) # []
