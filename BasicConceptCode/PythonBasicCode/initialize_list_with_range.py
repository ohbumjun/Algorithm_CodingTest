# 주어진 범위 만큼의 list를 만들어라
def initialize_list_with_range(end,start = 0, step = 1):
    return list(range(start, end +1, step))

initialize_list_with_range(5) # [0,1,2,3,4,5]
initialize_list_with_range(7,3) # [3,4,5,6,7]