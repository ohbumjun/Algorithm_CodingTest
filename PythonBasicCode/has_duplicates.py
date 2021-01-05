#list에 중복된 값이 있으면 true, 없으면 false 반환
def has_duplicates(1st):
    return len(1st) != len(set(1st))

# examples
x = [1,2,3,4]
y = [2,3,3,5]

has_duplicates(x) # false
has_duplicates(y) # true