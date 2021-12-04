# https://www.acmicpc.net/problem/10942

# 첫번째 풀이 : 혼자 풀이 --> 시간초과  ----
'''
< 사용방법 >
대칭 여부 확인
- 앞에서부터, 뒤에서부터 각각 오는 것 

a[i] == a[n-i-1] ?? 
그런데 착각하면 안되는 것이, 
만약 배열 길이가 n이라면

이렇게 대칭여부를 확인하는데 걸리는 시간복잡도가
O(n//2)가 아니라는 것이다 

모든 원소를 다 접근해서 검사하는 원리이기 때문에
O(n)이 되는 것이다 
'''
import sys
n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    st, ed = map(int, input().split())
    tmp = a[st-1:ed]
    ok = True
    rg = (ed-st)//2
    for i in range(rg+1):
        if tmp[i] != tmp[len(tmp)-1-i]:
            ok = False
            break
    if ok == True:
        print(1)
    else:
        print(0)

#  백준 풀이 ----
# 1) Top - Down
'''
위와 같은 문제방식으로 접근하게 되면
시간복잡도 O(NM)을 가지게 된다 

그런데 이 문제의 경우, 최대 20억 시간이 걸리므로
안된다 !!

다이나믹 프로그래밍.을 이용하려고 한다
1 2 3 2 4 2 3 2 1

여기서 우리는 해당 수열이 팰린드롬인지 아닌지를
확인하는 재귀적인 방법을 발견할 수 있다 

어떻게 ??
위의 배열을 idx상으로 보게 되면
idx : 1 2 3 4 5 6 7 8 9 로 바꿀 수 있다

그리고, 아래와 같은 재귀방식을 생각해낼 수 있다
1 == 9 && 2 ~ 8 가 팰린드롬인지 
...
...

즉, 원래 문제에서
재귀적으로 idx 만 작아지게 하면서, 
정답을 구해나갈 수 있다는 것이다 

>>
d[i][j] : a[i] ~ a[j] 까지가 팰린드롬이면 1, 아니면 0
- a[i] == a[j] 이 같아야 한다               : 첫번째 조건 
- a[i+1] ~ a[j-1] 까지가 팰린드롬이어야 한다 : 두번째 조건 ==> "d[i+1][j-1] == 1" 이어야 한다 

결과적으로 n개의 행,n개의 열로 구성된 d[i][j] 라는 2차원 행렬의 값을 채워넣는 과정이기 때문에
d(n^2)라고 할 수 있다 

>>
d[i][i] = 1 // 길이가 1인 부분수열은, 반드시 팰린드롬.이다 
>>
a[i] == a[i+1] // 길이가 2인 부분 수열은, 두수가 같을 때만 팰린드롬.이다 

---------------------------------------------------------------------------------------
이렇게 딱 한번만 세팅해두고 나면
O(n^2)라는 시간이 소요되며, 

이후, m개의 질문이 들어오면
그냥 d[i][j] 가 0인지 1인지만, 기존에 세팅해둔 정보를 보고 판단해주면 되기 때문에

결과적으로
O(n^2 + m) 이라는 시간이 걸리게 된다 
'''
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [[-1]*n for _ in range(n)]

# d[i][j] : -1 --> 답을 구하지 않은 상태
# d[i][j] : 0 : 팰린드롬 x
# d[i][j] : 1 : 팰린드롬 o


def go(i, j):  # i ~ j 까지의 부분수열이 팰린드롬인지 아닌지를 판단해주는 함수
    if i == j:  # 길이 1 --> 무조건 팰린드롬
        return 1
    elif i+1 == j:  # 길이 2
        if a[i] == a[j]:  # 같을때 --> 팰린드롬
            return 1
        else:  # 팰린드롬 x
            return 0
    if d[i][j] != -1:
        return d[i][j]
    # d[i][j]가 성립하기 위해서는 2가지 조건이 필요하다
    # 1) a[i] , a[j]가 같아야 하고
    # 2) a[i+1] ~ a[j-1]까지가 팰린드롬이어야 한다
    if a[i] != a[j]:  # 첫번째 조건에 해당하지 않는다면
        d[i][j] = 0
    else:  # 첫번째 조건은 해당한다면, 2번째 조건 고려
        d[i][j] = go(i+1, j-1)
    return d[i][j]


m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(go(s-1, e-1))  # 입력값을 idx 개념으로 바꾸려면 -1을 해주어야 하기 때문이다

# 2) Bottom-Up 방식
# 반복문을 사용하는 방식
'''

재귀호출 없이 풀 수 있다
길이가 1인 d[i][j]를 채우고
길이가 2인 것을 채우고
길이가 3인 것을 채우고 ( 길이가 1인 것을 이용하여, 양쪽 원소 추가하며 이용 )
길이가 4인 것을 채우기 ( 가운데 2개가 팰린드롬인지 검사 + 양쪽 원소 2개가 같은지 비교하기 )
n-1 인 것을 채우는 방식을 이용하면, for문으로도 채울 수 있다

'''
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [[0]*n for _ in range(n)]
for i in range(n):
    d[i][i] = True
for i in range(n-1):
    if a[i] == a[i+1]:
        d[i][i+1] = True
for k in range(3, n+1):  # k : 수열의 길이를 의미한다
    for i in range(0, n-k+1):  # i : 시작점.을 의미한다
        j = i+k-1  # j : 끝점
        if a[i] == a[j] and d[i+1][j-1]:  # 시작점, 끝점 같고, 그 안에가 팰린드롬인지 검사하기
            d[i][j] = True
m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(1 if d[s-1][e-1] else 0)

'''
C++ 

#include <cstdio>
int n;
int a[2000];
bool d[2000][2000];
int main() {
    scanf("%d",&n);
    for (int i=0; i<n; i++) {
        scanf("%d",&a[i]);
    }
    for (int i=0; i<n; i++) {
        d[i][i] = true;
    }
    for (int i=0; i<n-1; i++) {
        if (a[i] == a[i+1]) {
            d[i][i+1] = true;
        }
    }
    for (int k=3; k<=n; k++) {
        for (int i=0; i<=n-k; i++) {
            int j = i+k-1;
            if (a[i] == a[j] && d[i+1][j-1]) {
                d[i][j] = true;
            }
        }
    }
    int m;
    scanf("%d",&m);
    while (m--) {
        int s, e;
        scanf("%d %d",&s,&e);
        printf("%d\n",d[s-1][e-1]);
    }
    return 0;
}

'''
