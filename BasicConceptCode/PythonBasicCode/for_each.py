# list의 모든 값에 처음 부터 주어진 함수를 실행하세요
def for_each(str, fn):
    for el in str:
        fn(el)

for_each([1,2,3], print)