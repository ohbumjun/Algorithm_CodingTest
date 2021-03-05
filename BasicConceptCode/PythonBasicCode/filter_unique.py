# list에서 고유한 값을 필터링해라
from collections import Counter

# Counter : 리스트의 모든 값의 개수를 dictionary로 가져올 수 있다
# 이중에서 값의 개수가 1인 것만을 가져온다

def filter_non_unique(ArrayFirst):
    return [item for item , count in Counter(ArrayFirst).items() if count ==1]

print(Counter([1,2,2,3,4,4,5]))
print(Counter([1,2,2,3,4,4,5]).items())

for item, count in Counter([1,2,2,3,4,4,5]).items():

  print("item", item)
  print("count", count)

# examples
print( filter_non_unique([1,2,2,3,4,4,5]) ) # 1, 3, 5 