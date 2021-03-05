# list에서 개수가 가장 많은 값을 반환하세요
def most_frequent(list):
    return max(set(list), key = list.count)
    # 1) 일단 set 함수 사용을 통해, 고유값들을 가져온다
    # 2) max 함수로 최댓값을 가져온다. key를 list.count 로 설정하면, 개수가 가장 많은 값을 가져온다

# examples
most_frequent([1,2,3,3,2,4,4,1,2,8])