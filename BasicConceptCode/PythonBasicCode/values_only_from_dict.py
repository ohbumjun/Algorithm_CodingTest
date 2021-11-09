# 딕셔너리의 모든 값을 list로 전환하세요
def values_only(flat_dict):
    return list(flat_dict.values())

# examples
ages = {
    "Peter" : 10,
    "Isabel" : 11,
    "Anna" : 9
}

values_only(ages) # [10, 11, 9]