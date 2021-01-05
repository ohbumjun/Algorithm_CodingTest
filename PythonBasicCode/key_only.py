# 딕셔너리의 모든 키를 리스트로 전환해라
def keys_only(flat_dict):
    return list(flat_dict.keys())

# examples
ages = {
    'Father': 10,
    'Mother': 1,
    'Son': 2
}

keys_only(ages)