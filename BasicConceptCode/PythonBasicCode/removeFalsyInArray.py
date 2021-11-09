def compact(1st):
    return list(filter(None,1st))

# falsy value : 0, "", false, none 
# filter : 특정 조건에 일치하는 값만을 돌려주는 함수
# filter 첫번째 인자에 none, 2번째 인자에 1st를 넣어주면, falsy value를 제거할 수 있다


# example
compace([0,1, false, 2, 34]) # [1,2,34]