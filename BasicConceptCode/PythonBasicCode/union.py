# 두 리스트에 하나라도 존재하는 모든 값들을 가져와라
def union(a,b):
    return list(set(a+b))
    # a + b : 두개의 list를 합한다
    # set : 중복 제거하여 unique한 값을 가져온다

# examples
union([1,2,3],[4,3,2]) # [1,2,3,4]