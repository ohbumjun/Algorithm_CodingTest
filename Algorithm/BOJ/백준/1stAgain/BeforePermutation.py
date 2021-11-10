# 순열 크기 상, 이전 크기의 순열을 구하는 코드
# 순열은, 서로 다른 숫자들 끼리의 조합을 이용하여 순서를 정하는 것
# 즉, 중복은 허용되지 않는다

# 이전 크기의 순열을 찾기
# 위 원리의 반대를 생각하면 된다
# 뒤에서 올수록 작아져야 하는데 큰 숫자 , 즉, inverse_point를 구한다
def prev_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] >= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True
