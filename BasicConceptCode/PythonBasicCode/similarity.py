# 두리스트에 모두 있는 값의 리스트를 가져와라
def similarity(a,b):
    return [item for item in a if item in b]

# examples
similarity([1,2,3], [1,2,4]) # [1,2]