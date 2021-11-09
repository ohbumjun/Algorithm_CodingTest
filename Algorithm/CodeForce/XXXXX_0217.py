# https://codeforces.com/problemset/problem/1364/A

'''
>> What is Subarray ? -----------------

먼저 subarray의 정의를 봐야한다
subarray를 어떤식으로 정의할 수 있을까 ? 

전체 array에서 몇개의 element 들을
앞 혹은 뒤.에서 제거해 나가 생기는
array를 의미한다 .
중간에서 제거해나가는 방식이 아니다. 

ex [ 1, 2, 3 ]
의 subarray는
[1,2], [2,3] 가 될 것이다 
2라는 중간값을 제거해서 생긴 [1,3]은
subarray가 아니다 

아무것도 제거하지 않은
[1,2,3]도 subarray가 될 수 있다

즉, subarray는 중간에 있는 요소가 아닌
처음, 끝에서의 요소를 제거해서 생긴 
배열을 의미한다. 

>> 해결방법 : 2개의 point를 둔다 ------------

l pointer : 처음 - 1 ( idx ) ( 보통 placeholder, 혹은 centinal 이라고도 부른다 )
r pointer : 마지막 ( idx )

1번째 경우 : 모든 number가 x로 나누어질 수 있을때
ex. 7 7 7 ... : 모두 7 ! 
그리고 x = 7

이때는 그 어떤 subarray라고 하더라도 x로 나누어떨어진다
이 경우는 -1 을 return한다

2번째 경우 : 주어진 arr를 모두 더한 후, x로 안나누어 떨어지면, 이게 최대 length
따라서 원래 arr의 길이를 return한다

3번째 경우 : sum(arr)이 x로 나누어떨어지면, 이때 비로소 투포인터 방식을 활용한다

7 5 2 가 있다고 해보자

해당 arr의 합은 7( x )로 나누어 떨어진다.

만일 2를 제거하여 [ 7, 5 ] 라는 subarray를 만들게 된다면
이는 x로 나누어 떨어지지 않는 최대 subarray가 된다

즉, 기존 arr에서 x로 나누어떨어지지 않는 요소를 하나만이라도 제거하면
나머지 요소들의 합은, x로 나누어떨어지지 않게 된다 

이 원리에 기초하여 다음의 arr을 살펴보자
7 7 5 2 7 7 7

해당 arr의 합은 x ( 7 )로 나누어떨어진다
subarray가 앞 혹은 뒤의 요소들을 제거해서 생기는 것. 이라는 정의에 기초하면

앞에서부터 혹은 뒤에서부터 요소들을 제거해가면서
나머지 요소들의 합이 x ( 7 )로 나누어떨어지는지를 확인해 볼 수 있다

앞의 3개 ( 7 , 7, 5)를 제거할 때
5는 x ( 7 )로 나누어 떨어지지 않는 수이다.

이로 인해 나머지 element들 [ 2, 7, 7, 7] 의 합은
x로 나누어 떨어지지 않게 된다 

결국 앞에서부터 요소를 제거할 때, x로 나누어떨어지지 않는
가장 긴 subarray는 [ 2, 7, 7, 7 ] 이 되는 것이다

반면 !
뒤에서부터 요소 4개를 제거했다고 해보자 ( 7, 7, 7, 2)
2 역시 x( 7)로 나누어 떨어지지 않는 수이다

그렇다면 남은 element들 [ 7, 7, 5 ] 역시
x로 나누어 떨어지지 않는 가장 긴 subarray가 될 것이다 

결국 뒤에서부터 요소를 제거할 때, x로 나누어 떨어지지 않는
가장 긴 subarray는 [ 7, 7, 5 ] 이 되는 것이다.

즉, sum(arr)가 x로 나누어 떨어지지 않을 때, 
앞에서부터 요소를 제거해가면서 생긴 subarray, 
뒤에서부터 요소를 제거해가면서 생긴 subarray 

이 2개를 비교하여, 더 긴 length를 return하면 되는 것이다 


'''

import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

for _ in range(n):
    length, x = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    l = -1
    r = len(arr) - 1

    # sum이 x로 나누어떨어지지 않으면 arr 자체가 최대 length
    if sum(arr) % x != 0 :
        print ( len(arr) )
        continue
    
    # x로 나누어떨어지지 않는 맨 왼쪽, 맨 오른쪽 element를 찾는다
    for i in range(len(arr)) :
        if arr[i] % x != 0 :
            if l == -1 :
                l = i
            r = i
    # l == -1 이라는 것은, 모든 element가 x로 나누어떨어진다는 것 : -1 return
    if l == -1 :
        print( -1 )
        continue
    else :
        
        # 오른쪽, 왼쪽 제거된 subarray중 최대값 출력
        print( length - min( l + 1 ,  length - r ) )
        continue
        
    
        

    
    


    
        
