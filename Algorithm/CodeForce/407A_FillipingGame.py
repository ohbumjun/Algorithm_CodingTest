# https://codeforces.com/problemset/problem/327/A

# DP

'''

Kadane's algorithm
1) subarray
2) maximize or minimize sth

여기에서는 1의 개수를 maximize하는 과정이 필요하다.

우리는 0 과 1이 있다.
1의 개수를 늘린다는 기준에서 보면
0을 뒤집으면 1의 개수 + 1
1을 뒤집으면 0의 개수 - 1
만약 뒤집지 않으면    + 0
인 것이다.

자 이게 subarray의 문제라면, 
매 항목의 원소들을 만날 때마다 , 
해당 원소를 뒤집을 것인지 아닌지를 판단하는 것이다.

1의 개수를
가장 많이 늘릴 수 있는
뒤집기 set ! 
subarray를 구하는 것 .

우리가 할일 
1. 처음 1의 개수를 구한다
2. 0, 1 을 각각 1, -1 로 변환한다 ( 1의 개수 증감 관점 )
3. kadane algorithm 개념 : 1의 개수를 늘리기 위해
- 현재 만난 애도 뒤집을지
- 현재 만난 애는 안뒤집을지


- dy[j] : i번째 ! flip 고려했을 때, 증가하는 1의 최대치 

> 즉, dy[j]는 "1의 중가"라는 관점에서 봤을 때, 
j번째 원소를 증가시킬지 말지 결정하는 것 
1을 만나면 무조건  , 뒤집기 set 포함

> -1 을 만나면, 고려해야 한다 . 뒤집어서, 이전의 뒤집기 set, 
이전의 뒤집기 subarray에 포함시키더라도 ,
얘를 뒤집는 것을 포함한 subarray가 1을 여전히 증가시키는 거라면 포함

그러나, 얘를 현재 뒤집었는데 오히려 전반적으로 1이 감소한다 ? 
그러면, 여기서 이전까지의 뒤집기 subarray를 끝내고
+ 얘도 안뒤집어야 겠지 .
그리고 그 시점에서 새로운 subarray를 시작하는 것이다 . 그리고 
이 순간 만큼은 해당 요소에서 subarray에서 시작하고, 해당 요소에서 끝나느 것
즉, 이전의 모든 subarray를 다 끊어버리고
나 혼자 자신만이 최고의 subarray이다

그 반대는, 이전에서 이어온 subarray를 이어받아서
합쳐놓은 값이, 결국 최고의 subarray이다 

즉, 현재 얘가 subarray set의 마지막 요소라면 ,
그때의 최대 1 증감은 얼마가 되는 것이냐 !


즉, 비교 기준은 
0 ( 현재 얘를 안뒤집을 것인지 = 1의 증가가 없을 때 )
dy[j] + a ( 얘까지 뒤집어서 1의 개수를 증가시킬 것인지 )
둘 중 하나를 판단해야 하며 
ex . localMax = max( 0 , localMax + x )

지금까지의 subarray 중, 즉 뒤집기 set 중
1을 가장 많이 증가시켜온 set의 1 최대 증가 개수도 저장
maxSubSum = max( maxSubSum , dy[j] )

그리고 결과적으로 
우리가 구한 maxSubSum은
뒤집었을 때 증가하는 1의 개수이다.

그래서 기존의 1의 개수 + maxSubSum을 해주면 된다.

ex. 1 0 0 1 이라는 set가 있다고 할 때, 
가운데 2개의 0 을 뒤집으면 전체 1의 개수가 2 증가하고
이게 증가하는 1의 최대치

그래서 기존 1의 개수  = 2
+ 2

정답 : "4"

!! 단, 한가지 고려할 사항이 있다.
무조건 하나는 뒤집어야 한다. 
( 뒤집는 idx 범위 1 <= ~~ <= n )

즉, 만약 모든 원소 개수가 1 이라면 ,
하나는 뒤집어야 하므로,
처음 총 1의 개수 -1을 해주어야 한다.

'''

n         = int(input())
arr       = list(map(int, input().split()))
numOne    = 0
localMax  = 0
globalMax = 0
answer    = 0 

# 기존 1의 개수 + 모두 ( 1, -1 ) 로 바꿔주기
for i in range(len(arr)) :
    if arr[i] == 1 :
        numOne += 1
        arr[i] = -1
    else:
        arr[i] = 1
        
if numOne == n:
    answer = numOne - 1
    print(answer )
    
else:
    # 1의 개수를 최대로 증가시키는 flip set 구하기 ( subarray ) 구하기
    for elem in arr :
        localMax  = max( 0, localMax + elem )
        globalMax = max( localMax, globalMax )

    answer = globalMax + numOne
    print(answer )



