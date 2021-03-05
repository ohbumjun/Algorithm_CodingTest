#주어진 개수의 값을, 리스트의 끝으로 이동시키기
def offset(1st, offset):
    return 1st[offset:] + 1st[:offset]
    # slice기법을 통해, 주어진 개수만큰 slice
    # 나미저애를 더해서 합친다

# examples
offset([1,2,3,4,5], 2) # [3,4,5,1,2]
offset([1,2,3,4,5], -2) # [4,5,1,2,3]