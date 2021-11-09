# 주어진 값으로 채워진 list 를 만들어라
def initialize_list_with_values(n, val = 0) : # 값이 빌수도 있다. 그럴때는 0으로 채워준다
    return [val for x in range(n)] # n번 만큼 반복하면서, 해당 val을 list안에 넣는다

# examples
initialize_list_with_values(5,2) # [2,2,2,2,2] > 2라는 값이 5번 채워진 list를 만들어라 

