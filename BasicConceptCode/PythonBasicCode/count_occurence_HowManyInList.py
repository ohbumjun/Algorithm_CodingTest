# 배열에서 해당 조건에 맞는 요소들이 몇개있는지를 보기
def count_occurence(1st, val) :
    return len([ x for x in 1st if x == val and type(x) == type(val)])
# 코드 분석
# 1) x == val and type(x) == type(val) : 값과 ,type이 같은 것을 확인하기
# 2) list comprehension을 통해, for문을 돈다
# 3) 그러한 조건에 맞는 것을 맨 앞 x 에 넣고
# 4) [ ] 그러한 x 들에 대한 배열을 만들고
# 5) len을 통해, 총 개수를 구한다 
 
# examples
count_occurences([1,2,3,1,2,1], 1) # 해당 list에서 1이 몇개있는가 