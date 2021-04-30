'''
2가지 핵심 포인트가 존재한다
1) 넣는 방법의 수를 어떻게 구할 것이며
2) 그 많은 무게 종류를 dp로 가능하냐는 것이다.

사실, 생각해보면
subsum 개수를 구하는 문제이다.

일반적으로 subsum 중에서,
그중에서도 maximum subsum을 구하는
대표적인 알고리즘이 바로
' meet in the middle ' 알고리즘 이다. 

< meet in the middle >
https://www.youtube.com/watch?v=wqk6U6lERZA

어떤 set A 가 있고 { a1, a2, ...an}  까지 원소가 존재한다고 하자.

우리는 set A에서, 10 ^ 5를 넘지않는,  maximum sum subset ( 최대 합을 가지는 부분 수열)을 찾고 싶다.

1. Brute Force : O ( 2 ^ n ) -------------------------------
왜 ? 결국은 Brute Force 입장에서는
원소 각각이 부분수열에 포함되느냐, 안되느냐를 판단하는 
즉, 원소 하나마다 2가지의 경우를 고려하는 것이므로

2 ^ n ( 원소 개수 ) 가 되는 것이다.

2. Meet in the middle -------------------------------------

2_1 ) 정확하게 앞 n / 2 , 뒤 n / 2 개의 원소로 나눈다
A  = [ a1 .... a 2/n ]
B  = [ b1 .... b 2/n ]

2_2) 
A 에 대해서 가능한 부분수열을 구해놓는다
완전탐색을 사용한다
2 ^ ( n / 2 ) 인 all subset sum 을 구해놓는다.

B도 같은 작업을 진행한다.

2_3) 이제 B를 sort 한다.
B에서 뽑아낸, all subset sum 들의 집합을 살펴보자. 

all subset sum의 개수는 2 ^ ( n // 2) 개 였다.
sort에서의 최소 시간 복잡도는 O ( k log k )

그래서 결국 B set의 all subset sum 들의 집합을 sort하는데에는
2 ^ ( n // 2 ) * log ( 2 ^ (n //2) ) 가 걸릴 것이다.

== ( n ) *  ( 2 ^ (n//2) )

2_4)
자. 이제 A의 all subst sum들 집합의 원소
하나하나에 대해서

sort 해둔 B all subset sum 집합을, 이진 탐색하면서 ( 참고 : 이진 탐색의 조건 == 정렬 )

현재 A의 subset sum 하나의 원소 + sort된 B all subset sum에서 이진탐색 된수 == max 가 되는 값을
찾는 것이다.

그러면서, 최대값을 기록하고, 계속 갱신해간다. 

2_5) 이 과정에서 시간복잡도는 ( 2 ^ ( n  // 2  ) ) * ( log ( 2 ^ ( n //2 ) ) ) 가 된다.
즉, n * 2 ^ ( n // 2 ) 가 되는 것이다.

왜 ?
sort된 B all subset sum 집합을 한번 이진탐색할때 ( 이진탐색 시간복잡도 : log k) > log ( 2  ^  n // 2)
그리고, 그것으 2 ^ ( n // 2 ) 개의 A all subset sum 원소들에 대해 적용하기 때문이다

'''

# 첫번째 풀이 : 오답 -------------------------------------------------------------------------------
from collections import deque, Counter
import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)


def a_BF(v):
    # v : 특정 원소 idx
    if v == len(a_Arr):
        tmpArr = []
        for i in range(len(a_Arr)):
            if a_ch[i] == 1:
                tmpArr.append(a_Arr[i])
        a_sumArr.append(sum(tmpArr))
    else:
        # 사용한다 = 1, 사용하지 않는다 = 0
        a_ch[v] = 1
        a_BF(v + 1)
        a_ch[v] = 0
        a_BF(v + 1)


def b_BF(v):
    # v : 특정 원소 idx
    if v == len(b_Arr):
        tmpArr = []
        for i in range(len(b_Arr)):
            if b_ch[i] == 1:
                tmpArr.append(b_Arr[i])
        b_sumArr.append(sum(tmpArr))
    else:
        # 사용한다 사용하지 않는다
        b_ch[v] = 1
        b_BF(v + 1)
        b_ch[v] = 0
        b_BF(v + 1)


def lower_bound(start, end, target):

    global cnt

    while start < end:
        mid = (start + end) // 2
        if b_sumArr[mid] > target:
            end = mid
        elif b_sumArr[mid] <= target:
            start = mid + 1
        else:
            end = mid
            break

    return end


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().split())
    inputArr = list(map(int, sys.stdin.readline().strip().split()))
    cnt = 0

    a_Arr = inputArr[: len(inputArr) // 2]
    b_Arr = inputArr[len(inputArr) // 2:]

    a_sumArr = []
    b_sumArr = []
    a_ch = [0] * (len(a_Arr))
    b_ch = [0] * (len(b_Arr))

    # a, b 이진 탐색
    a_BF(0)
    b_BF(0)

    # b sort
    a_sumArr.sort()
    b_sumArr.sort()

    # a_sumArr 의 각 원소에 대해, b_sumArr 이진탐색하면, 찾아내기
    for i in a_sumArr:
        if C - i < 0:  # == 0인 경우를 고려하지 않는 이유는 b_sumArr에 0이 포함된 경우도, 더해주기 위해서이다
            continue
        else:
            # return value of "upper_bound" function will be, at which position, least target value is located
            # for ex) if '1' is target, and it's idx == 1 > it means, '0' which is in front of '1' can be also answer
            # so, return value should be '2' , so that, we can say
            # oh ! if target value is '1', then totally '2' values are possible !
            ans = lower_bound(0, len(b_sumArr), C - i)
            cnt += ans

    print(cnt)


# 두번째 풀이 : 정답 -------------------------------------------------------------------------------

def a_BF(v):
    # v : 특정 원소 idx
    if v == len(a_Arr):
        tmpArr = []
        for i in range(len(a_Arr)):
            if a_ch[i] == 1:
                tmpArr.append(a_Arr[i])
        a_sumArr.append(sum(tmpArr))
    else:
        # 사용한다 = 1, 사용하지 않는다 = 0
        a_ch[v] = 1
        a_BF(v + 1)
        a_ch[v] = 0
        a_BF(v + 1)


def b_BF(v):
    # v : 특정 원소 idx
    if v == len(b_Arr):
        tmpArr = []
        for i in range(len(b_Arr)):
            if b_ch[i] == 1:
                tmpArr.append(b_Arr[i])
        b_sumArr.append(sum(tmpArr))
    else:
        # 사용한다 사용하지 않는다
        b_ch[v] = 1
        b_BF(v + 1)
        b_ch[v] = 0
        b_BF(v + 1)


def upper_bound(start, end, target):

    global cnt

    while start < end:
        mid = (start + end) // 2
        if b_sumArr[mid] <= target:
            start = mid + 1
        else:
            end = mid

    return end


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().split())
    inputArr = list(map(int, sys.stdin.readline().strip().split()))
    cnt = 0

    a_Arr = inputArr[: len(inputArr) // 2]
    b_Arr = inputArr[len(inputArr) // 2:]

    a_sumArr = []
    b_sumArr = []
    a_ch = [0] * (len(a_Arr))
    b_ch = [0] * (len(b_Arr))

    # a, b 이진 탐색
    a_BF(0)
    b_BF(0)

    # b sort
    a_sumArr.sort()
    b_sumArr.sort()

    # a_sumArr 의 각 원소에 대해, b_sumArr 이진탐색하면, 찾아내기
    for i in a_sumArr:
        if C - i < 0:  # == 0인 경우를 고려하지 않는 이유는 b_sumArr에 0이 포함된 경우도, 더해주기 위해서이다
            continue
        else:
            # return value of "upper_bound" function will be, at which position, least target value is located
            # for ex) if '1' is target, and it's idx == 1 > it means, '0' which is in front of '1' can be also answer
            # so, return value should be '2' , so that, we can say
            # oh ! if target value is '1', then totally '2' values are possible !
            ans = upper_bound(0, len(b_sumArr), C - i)
            cnt += ans

    print(cnt)


# --------------------------------------------------------------------------------------------------------
'''
다른 점 ?

1) upper_bound가 아니라 lower_bound를 실시한 것 
2) upper_bound 함수 실행시 end 값 

1_1) 우선, lower_bound가 아니라, upper_bound를 실시해야 한다.
왜 ?? 우리가 예를들어, 1이라는 target를 찾는다고 해보자
우리는 1이라는 target보다 큰 값을 찾아야 한다 

왜 그럴까
우리는 b all subset sum에서, 가능한 후보군의 개수를 보는 것이다

예를 들어, b all subset sum = [ 0, 1, 2 ] 이고, 
c- i 가 1 이라면, 
1보다 작거나 같은 값들은 모두 값이 된다는 것
b all subset sum은 오름차순 정렬된 상태이기 때문에
결국 1까지 값이 2개이고, 2개가 답이 될수 있다라는 것을 return 해주려면
1의idx가 아니라, 1보다 큰, 그러면서 최소인 2의 idx를 찾아야 한다

1이라는 값을 포함한, 최소를 찾는 것이 아니라
1보다 큰 , 최소값을 찾는
upper_bound를 실행해야 한다.

1_2) 이건 lower_bound 함수 에 대한 것인데, lower_bound 함수에서 res[mid] == target 일때 break를 시켜버리면 안된다

    def upper_bound(start, end, target):
        
        global cnt
        
        while start < end :
            mid = ( start + end ) // 2
            if b_sumArr[mid] > target :
                end = mid
            elif b_sumArr[mid] <= target :
                start = mid + 1
            else:
                end = mid
                break
            
        return end

위와 깉이 
    else: 
        end = mid
        break

여기서 break를 시켜주면 안된다.
왜냐하면, 비록 같은 값을 지니는 value를, 
mid idx에서 찾았어도
해당 value, 즉, target이 중복되어
mid idx보다 
더 앞에 위치할 수도 있기 때문이다.


2) ans = upper_bound( 0 , len(b_sumArr) , C - i ) 에서

end 매개변수 자리에 들어가는 인자가
len(b_sumArr) - 1이 아니라
len(b_sumArr) 이 되어야 한다.

왜 ?
잘 생각해보자

b_sumArr = [ 0, 1 ] 이다
우리가 1까지는 포함되는 후보의 개수를 return 하려면
즉, 1보다 작거나 같은 모든 값은 선택될 수 있으며 ,
결국 0과 1, 
총 2개 ! 라는 개수를 return 해야 한다

그런데 만일 
len(b_sumArr) - 1을 end 값으로 넣어버리면
end,
즉, upper_bound 함수가 리턴할 수 있는 최대값이 1로 한정되어 버린다.

결국, 맨 마지막 값, 이상의 idx를 표현하기 위해서
2라는 값을 return할 수 있도록 하기 위해서

len(b_sumArr) 을 , 2를, 최대 return할 수 있는 범위로 설정해주는 작업이다 

'''
