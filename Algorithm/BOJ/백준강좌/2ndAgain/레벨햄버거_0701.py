#

# 처음 코드
n, x = map(int, input().split())
dp = [0]*(n+1)  # n버거 구성

dp[0] = 'P'
for i in range(1, n+1):
    dp[i] = 'B' + dp[i-1] + 'P' + dp[i-1] + 'B'

ans = 0
for i in range(x):
    if dp[n][i] == 'P':
        ans += 1
print(ans)

'''
위의 과정이 답이 될 수 없는 이유는 무엇일까 ?

바로 ,
매번 배열의 한 element에 들어가는 원소의 개수가
*2 로 증가하는데

10번만 거쳐도 2^10
즉, 너무 많은 문자열이 저장되어버린다는 것이다 
따라서, 실제 만드는 것은 불가능하다는 것이다 

'''

n, x = map(int, input().split())
d = [0]*(n+1)
p = [0]*(n+1)
d[0] = 1
p[0] = 1

for i in range(1, n+1):
    d[i] = 1 + d[i-1] + 1 + d[i-1] + 1
    p[i] = p[i-1] + 1 + p[i-1]


def go(n, x):
    if n == 0:
        if x == 0:
            return 0
        else:
            return 1
    elif x == 1:
        return 0
    elif x <= 1 + d[n-1]:
        return go(n-1, x-1)
    elif x == 1 + d[n-1] + 1:
        return p[n-1] + 1
    elif x <= 1 + d[n-1] + 1 + d[n-1]:
        return p[n-1] + 1 + go(n-1, x-1-d[n-1]-1)
    else:
        return p[n-1] + 1 + p[n-1]


print(go(n, x))


'''
D[i] : 레벨 i 햄버거의 길이 ------------

레벨-0 햄버거는 패티
- d[0] = 1
- d[n] = 1 + d[n-1] + 1 + d[n-1] + 1 = 2*d[n-1] + 3

P[i] : 레벨 i 햄버거의 패티 개수 -------
레벨 0 햄버거는 패티
- p[0] = 1
- p[i] = p[i-1] + 1 + p[i-1] = 2 * p[i-1] + 1


go(N,X) -------------------------------

레벨 N 햄버거의 아래 X 장 먹었을 때
먹은 패티의 수

1) N이 0인 경우, -----------------------
x = 0이면 0 , 그 외에는 1

2) N > 0 , x == 1 인 경우, -------------
0 ! ( 왜냐하면, 맨 앞에는 햄버거번 only )

3) 레벨 N-1 버거 -----------------------
1 <= x <= 1 + d[n-1] 

햄버거번 + (레벨n-1 버거)

이 중에서 아래 x개를 조사한다는 것은
다시 말하면, 햄버거번 맨 앞에것을 제외

레벨n-1 버거 제엇, x-1 개를 조사한다는 것과
동일한 의미이다 

4) 레벨 N-1 버거 ----------------------
1 <= x <= 1 + d[n-1] + 1

즉, 햄버거번 + 레벨n-1버거 + 패티
까지 고려한다면

p[n-1] (n-1개중에서 패티 개수) + 1
이 정답이 될 것이다 

4) 레벨 N-1 버거 ----------------------
1 <= x <= 1 + d[n-1] + 1 + d[n-1]

즉, 햄버거번 + 레벨n-1버거 + 패티 + 레벨n-1버거 일부
까지 고려한다면

p[n-1] (n-1개중에서 패티 개수) + 1 + go(N-1,x-1-D[n-1]-1)

즉, 2번째 레벨n-1버거 중에서
총 x - 그 앞의 것들 구성 (햄버거번 + 레벨n-1버거 + 패티)
을 뺀 패티의 수. 라고 할 수 있다 


즉
시간복잡도를 따져보면
1) D 배열을 구하는 시간 O(n)
2) P 배열을 구하는 시간 O(n)
3) go 재귀함수를 돌리는 시간 O(n)
하여 총 
O(n) 만큼의 시간이 소요된다 

5) 레벨 N-1 버거 ----
x == 1 + d[n-1] + 1 + d[n-1] + 1

즉, 햄버거번 + 레벨n-1버거 + 패티 + 레벨n-1버거 + 햄버거번
모두를 포함하는 경우를 의미한다 

p[n-1] + 1 + p[n-1]

'''


# C++
'''
#include <iostream>
using namespace std;
long long d[51];
long long p[51];
long long go(int n, long long x) {
    if (n == 0) {
        if (x == 0) {
            return 0;
        } else {
            return 1;
        }
    } else if (x == 1) {
        return 0;
    } else if (x <= 1 + d[n-1]) {
        return go(n-1, x-1);
    } else if (x == 1 + d[n-1] + 1) {
        return p[n-1] + 1;
    } else if (x <= 1 + d[n-1] + 1 + d[n-1]) {
        return p[n-1] + 1 + go(n-1, x-1-d[n-1]-1);
    } else {
        return p[n-1] + 1 + p[n-1];
    }
}
int main() {
    int n;
    long long x;
    cin >> n >> x;
    d[0] = 1;
    p[0] = 1;
    for (int i=1; i<=n; i++) {
        d[i] = 1 + d[i-1] + 1 + d[i-1] + 1;
        p[i] = p[i-1] + 1 + p[i-1];
    }
    cout << go(n, x) << '\n';
    return 0;
}
'''
