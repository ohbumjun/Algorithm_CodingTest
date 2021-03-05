# list에서 랜덤하게 값을 가져오세요
from random import randint # 해당 라이브러리로 부터, 랜덤하게 숫자를 만드는 함수를 가져온다


def sample(1st):
    return 1st[randint(0,len(1st) -1)]
    # randint(0, len(1st) -1) : 0부터 len(1st)-1 까지의 정수중 랜덤하게 값을 가져온다


# examples
sample([3,7,9,11]) # 9