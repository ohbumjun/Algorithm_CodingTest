# 끝에서부터 n개의 값을 가져와라
def take_right(itr, n = 1) :
    return itr[-n:] # start가 -n 이라는 것은, 뒤에서부터 n번째 부터 start 한다는 것이다

# examples
take_right([1,2,3], 2) # [2,3]
take_right([1,2,3])

