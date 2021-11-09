# https://www.acmicpc.net/problem/11058

'''
1. 화면에 출력한다

< 1번째 경우 >
--> 출력 한개 증가하기 
D[n] = D[n-1] + 1

2,3 : 화면 출력에는 아무런 영향을 주지 않는다


4 : 버퍼가 비어있지 않은 경우에만 의미가 있다. 
즉, 버퍼에 무언가를 넣어주어야 한다는 것이다 
그리고 버퍼에 넣으려면 선택을 해야 한다
즉, 적어도 한번은 ctrl+A , ctrl+C, ctrl+V 가 연속으로 눌러져야 한다 

< 2번째 경우 >
--> N번 눌렀다고 했을 때 , 마지막 3번 연속 누르고 + D[N-3] 
즉, D[N] = D[N-3] * 2


< 3번째 경우 >
ctrl + V를 연속으로 누르는 경우  
(N-4) A C V V 
그렇다면 앞의 N-4개의 내용이 총 3번 출력된다 
D[N] = D[N-4] * 3

ctrl + V를 3번 연속으로 누르는 경우 
(N-5) A C V V V 
그렇다면 앞의 N-5개의 내용이 총 4번 출력된다 
D[N] = D[N-5] * 4

.....

즉, 마지막에 V를 j번 누른 경우
D[N] = D[N-(j+2)] * (j+1)

j의 범위는 어떻게 정의할 수 있을까 ?
1) j = 1 보다는 크거나 같아야 한다( 적어도 한번은 누른 경우)
2) 최소의 경우 => 아무것도 출력안하고, 바로 A C V V V V V V ...
즉, ( A C V V V V V ..) : i번
j는 i-2보다는 작거나 같아야 한다는 것이다(버퍼에 비어있지 않기 위해 )
따라서 1 <= j <= i - 2 

< 시간 복잡도 > 
O(N ^ 2)
왜 ? 
총 N개의 답을 구해야 하는데
그때마다, 복붙 몇번했는지에 대한 j 들 모두에 대해서도
고려해야 하기 때문이다 

'''

n = int(input())
d = [0] * (n + 1)
d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    for j in range(1, i-1):
        d[i] = max(d[i], d[i-(j+2)] * (j+1))
print(d[n])

# 다른 풀이
n = int(input())
if n <= 3:
    print(n)
else:
    dp = [0] * (n+1)
    dp[1], dp[2], dp[3] = 1, 2, 3
    for i in range(4, n+1):
        dp[i] = max(dp[i-3]+3, 2*dp[i-3], 3*dp[i-4], 4*dp[i-5])

    print(dp[n])
