# list의 마지막 값부터 모든 값에 처음 부터 주어진 함수를 실행하세요
def for_each(str, fn):
    # str[::-1] : slicing 방법을 통해, 배열을 역순으로 정렬한다
    for el in str[::-1]:
        fn(el)

for_each([1,2,3], print)