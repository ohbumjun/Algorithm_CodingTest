# https://www.acmicpc.net/problem/10816


# 1. 기본적인 이분 탐색  --------------------------------------------------------------------------
n = int(input())
cards = sorted( list(map(int,input().split())) )
howMany = int(input())
targets = list(map(int,input().split())) 

def binarySearch( array, target, st, ed ):
    global cnt
    if st > ed :
        return 0

    mid = ( st + ed ) // 2

    if array[mid] == target :
        # mid가 아니라, st부터 고려하는 이유는, mid 바로 앞 값도 현재 mid값과 같을 수 있다
        # 그래서 아예 처음부터 search 하는 것이다 
        return array[ st : ed + 1].count(target)
    elif array[mid] > target :
        return binarySearch( array, target, st, mid -1 )
    else :
        return binarySearch( array, target, mid + 1 , ed )

'''
아래 for문은, cards 배열에서, 각 원소가 몇개 있는지를 count 하는 것이다.
이를 count하는 방식은 객체를 선언해두고, key ~ value pair 방식으로 저장한다.
그 다음 !! 

targets 배열의 원소를 다 돌면서
target이 곧 key로 들어가서, 그의 value값들을 출력하는 것이다.

'''
n_dict = {}
for card in cards :
    # 그저 'key' in 'dict'형태로, 현재 dict 안에 key에 해당하는 value가 저장되어있는지 확인가능하다
    if card not in n_dict :
        result = binarySearch(cards,card,0, len(cards) -1 )
        n_dict[card] = result

print( ' '.join( str(n_dict[x]) if x in n_dict else '0' for x in targets ) )  



# 2. 순서대로 숫자 세어나가기 ----------------------------------------------------------------------
'''
기본적인 원리는 다음과 같다.
cards, targets 를 모두 sorting한다

targets의 값들을 기준으로 차례대로 cards의 값들과 비교하게 되는데
targets[0] 인 애의 count를 센 다음
targets[1] 의 count를 셀 때는 index  이후의 cards를 탐색, 
즉, 탐색 범위가 뒤로 갈수록 점점 줄어드는 것을 확인할 수 있다.
'''
n = int(input())
cards = sorted( list(map(int,input().split())) )
howMany = int(input())
targets = list(map(int,input().split()))

_dict , index = {} , 0

for target in sorted(targets) :
    cnt = 0
    while index < len(cards) :
        if target == cards[index] :
            index += 1
            cnt   += 1
        elif target > cards[index] :
            index += 1
        else:
            break
    _dict[target] = cnt

print(' '.join( str( _dict[x] ) for x in targets  ) )
    


# 3. Hashing 해쉬 알고리즘 방식 ----------------------------------------------------------------------
n = int(input())
cards = sorted( list(map(int,input().split())) )
howMany = int(input())
targets = list(map(int,input().split())) 

hashmap = {}

for card in cards :
    if card in hashmap :
        hashmap[card] += 1
    else:
        hashmap[card] = 1

print( ' '.join( str(hashmap[x]) if x in hashmap else '0' for x in targets ) )


# 4. Collections 라이브러리의 Counter 함수  ----------------------
# Counter 함수
n = int(input())
cards = sorted( list(map(int,input().split())) )
howMany = int(input())
targets = list(map(int,input().split())) 

c = Counter(cards)

print( ' '.join( str(c[x]) if x in c.keys() else '0'  for x in targets ) )

