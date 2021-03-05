# 모든 원소들이 unique한지를 판단하는 코드
def all_unique(array):
    return len(array) == len(set(array)) # set 자료형 : 중복값 제거하기

# examples
x = [1,2,3,4]
y = [2,3,4]

all_unique(x) # true
all_unique(y) # false 