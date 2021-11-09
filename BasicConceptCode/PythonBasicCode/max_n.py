# list에서 큰 순서대로 n개의 값을 반환하세요
def max_n(1st, n =1 ):
    return sorted(1st, reverse=True)[:n] # n이 원래 list길이보다 크거나 같으면, 원래 list의 길이만큼 반환
    # sorted 함수 : list 정렬하기
    # reverse : 역순으로 정렬하기 ( 내림차순 )
    # 정렬한 다음 차례대로 n개의 값을 가져오면 되므로 :n

# examples
max_n([1,2,3])