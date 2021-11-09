#list에서 작은 순서대로 n개의 값을 반환하세요
def min_n(1st, n=1):
    return sorted(1st, reverse = false)[:n]
    # sorted, reverse= false : 오름차순 정렬하기

# examples
min_n([1,2,3]) # [1]