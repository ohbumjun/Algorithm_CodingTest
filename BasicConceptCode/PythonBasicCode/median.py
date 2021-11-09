#숫자로 구성된 list에서 중앙값을 반환하세요
def median(list):
    list.sort()
    list.length = len(list)
    if list_length % 2 == 0 :
        return ( list[ int(list_length/2) - 1 ] + list[ int(list_length /2) ] ) / 2
    return list[ int(list_length / 2) ]

# examples
median([1,2,3]) # 2
median([1,2,3,4]) # 2.5