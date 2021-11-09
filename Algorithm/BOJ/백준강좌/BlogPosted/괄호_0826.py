# https://www.acmicpc.net/problem/10422

# 1번째 풀이 ---
# 올바른 괄호 문자열에 집중
'''
1번째 조건 : 올바른 괄호 문자열 개수는 "짝"을 짓기 때문에, 항상 "짝수"가 나와야 한다
2번째 조건 : 앞에서부터 탐색한다고 했을 때, 여는 괄호 문자열이, 닫는 괄호 문자열보다 숫자가 작아지면 안된다
ex) '())' 이러한 경우는 없어야 한다는 것이다 

문제 풀이 방법
길이가 L인 문자열 배열이 있다고 해보자 

2번째 조건에 의해, 문자열 배열 첫번째 원소는 무조건 '('이 와야 한다

해당 '(' 에 대한, 닫는 괄호 짝이 i번째 원소에 위치한다고 해보자
'(' -- 전반부 올바른 괄호 문자열 -- ')' -- 후반부 올바른 괄호 문자열 --

즉, 길이가 L인 문자열 밸에 대해, 올바른 괄호 문자열 개수를 구하는 경우는
1) 처음 괄호 문자열 ~ 그에 대한 짝 i번째 괄호 문자열
2) 전반부 올바른 괄호 문자열 개수 
3) 후반부 올바른 괄호 문자열 개수 
를 모두 고려하는 경우와 같다

전반부 길이 : i - 2
후반부 길이 : L - i

d[L] : 길이가 L인 올바른 괄호 문자열의 개수. 라고 했을 때
d[L] = (합)(d[i-2] * d[L-i]) 이 된다. ( 2 <= i <= L)
왜 i의 범위가 2 <= i <= L 인 것일까 ??
i는 닫는 괄호의 위치,  제일 앞에오는 경우는 () --> 2번째
혹은 (.....) --> 이렇게 가장 마지막 올 수 있음 --> L번째 
뿐만 아니라, i는 무조건 '짝수' 가 될 것이다( 닫는 괄호의 위치 --> 해당 짝의 여는 괄호가 반드시 있어야 하므로 
즉, 무조건 짝수의 배수 형태이기 때문이다 )

d[L] = (합)(d[i-2] * d[L-i]) ?? 
왜 곱하기 ?? d[i-2]는 여러개의 올바른 괄호 문자열이 들어갈 수 있고,
각각에 대해서 또 d[L-i] 에 해당하는, 여러개의 가능한 올바른 괄호 문자열
'쌍'을 구해가는 과정이기 때문이다 

---
d[0]은 무엇일까 ?
길이가 0인 괄호 문자열의 개수는 1이 된다
왜 ??
올바른 문자열이 아닌 조건은 --> ()) 와 같은 것
그런데 길이가 0인 문자열 같은 경우
''이다. 
이또한 한편으로는 '올바른 문자열'이 아니지는 않다.
따라서 '올바른 문자열'이라고 치환할 수 있다

혹은, 아무것도 넣지 않는 경우수. 라는 1가지의 경우로 
치환해서 생각할 수도 있다는 것이다 

---
시간 복잡도 
O(L^2) : 각각의 L 마다, 2 <= i <= L 인, i를 고려해주어야 
하기 때문이다 

'''
mod = 1000000007
d = [-1] * 5001


def go(n):
    if n == 0:
        return 1
    if d[n] >= 0:
        return d[n]
    d[n] = 0
    for i in range(2, n+1, 2):
        d[n] += go(i-2) * go(n-i)
        d[n] %= mod
    return d[n]


t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(go(n))
    else:
        print(0)

'''
< C++ >
#include <iostream>
#include <cstring>
using namespace std;
long long d[5001];
long long mod = 1000000007LL;
long long go(int n) {
    if (n == 0) {
        return 1;
    } else if (d[n] >= 0) {
        return d[n];
    }
    d[n] = 0;
    for (int i=2; i<=n; i+=2) {
        d[n] += go(i-2) * go(n-i);
        d[n] %= mod;
    }
    return d[n];
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    memset(d,-1,sizeof(d));
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        if (n%2 == 0) {
            cout << go(n) << '\n';
        } else {
            cout << 0 << '\n';
        }
    }
    return 0;
}

'''

# -------------------------------------------------------------

# 2번째 풀이 ---
# 올바르지 않은 괄호 문자열에 주목
'''
길이 N이 주어졌을 때, 길이가 N인 
'올바른 괄호 문자열'의 개수를 구하는 문제

D[N][L] = 길이가 N인 '괄호 문자열', 짝이 맞지 않는
여는 괄호의 개수 = L개

길이가 N인 올바른 괄호 문자열 : D[N][0]

'''
mod = 1000000007
d = [[0] * 5001 for _ in range(5001)]
d[0][0] = 1
for i in range(1, 5001):
    for j in range(i+1):
        if j+1 <= i:
            d[i][j] += d[i-1][j+1]
        if j-1 >= 0:
            d[i][j] += d[i-1][j-1]
        d[i][j] %= mod
t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n][0])

'''
< C++ >
#include <iostream>
using namespace std;
long long d[5001][5001];
long long mod = 1000000007ll;
int main() {
    d[0][0] = 1;
    for (int i=1; i<=5000; i++) {
        for (int j=0; j<=i; j++) {
            d[i][j] = 0;
            if (j+1 <= i) {
                d[i][j] += d[i-1][j+1];
            }
            if (j-1 >= 0) {
                d[i][j] += d[i-1][j-1];
            }
            d[i][j] %= mod;
        }
    }
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        cout << d[n][0] << '\n';
    }
    return 0;
}
'''
