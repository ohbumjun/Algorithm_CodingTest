# https://www.acmicpc.net/problem/11066

'''
중요한 조건 
- 연속된 파일만 합칠 수 있다 
- 파일은 항상 '2개'의 연속된 파일을 합치는 것이다 //

a1 a2 a3 a4 a5 라는 파일 5개가 있다고 해보자

이렇게 5개의 파일을 합치는 방법은 4가지가 존재한다
(a1)(a2 a3 a4 a5)
(a1 a2)(a3 a4 a5)
(a1 a2 a3)(a4 a5)
(a1 a2 a3 a4)(a5)

즉, 파일의 개수 뿐만 아니라, "파일의 구성"도 중요하다는 점을 알 수 있다.
그리고 그러한 "파일의 구성"은 "연속된 파일들"로 구성되어 있다는 점도 알 수 있으며
"연속된 파일"은 '시작과 끝'을 이용하여 표현할 수 있다는 점도 알 수 있다

따라서 d[i][j]를 ai ~ aj 까지의 
파일들을 합치는 비용의 최소. 라고 정의할 수 있다 

그리고 뿐만 아니라, i ~ j 까지의 파일을 합치는 것은
이 또한, 연속된 파일 2개를 합치는 과정이며
i ~ k , k+1 ~ j
까지의 파일 목록을 합치는 것이라고도 할 수 있다 

따라서
d[i][j] = d[i][k] + d[k+1][j] +(a[i] ~ a[j] 까지의 합)
라고 할 수 있는 것이다 

i <= k 
k+1 <= j ( k < j )

즉, i <= k < j 로 정의되는 k 중에서
d[i][k] + d[k+1][j] 를 최소로 갖는 것을 d[i][j]를 정의할 때 사용하면 되는 것이다 


< 시간 복잡도 >
가능한 i 개수 : n개
가능한 j 개수 : n개

총 n ^ 2 개의 문제의 개수가 존재한다 
'''


def go(i, j):
    if i == j:
        return 0
    if d[i][j] != -1:
        return d[i][j]
    ans = d[i][j]
    cost = sum(a[i:j+1])
    for k in range(i, j):
        temp = go(i, k) + go(k+1, j) + cost
        if ans == -1 or ans > temp:
            ans = temp
    d[i][j] = ans
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = [[-1]*n for _ in range(n)]
    print(go(0, n-1))

'''
# include <cstdio>
# include <cstring>
int a[501]
int d[501][501]
int go(int i, int j) {
    if (i == j) {
        return 0
    }
    if (d[i][j] != -1) {
        return d[i][j]
    }
    int & ans = d[i][j]
    int sum = 0
    for (int k=i
         k <= j
         k++) {
        sum += a[k]
    }
    for (int k=i
         k <= j-1
         k++) {
        int temp = go(i, k) + go(k+1, j) + sum
        if (ans == -1 | | ans > temp) {
            ans = temp
        }
    }
    return ans
}
int main() {
    int t
    scanf("%d", & t)
    while (t--) {
        memset(d, -1, sizeof(d))
        int n
        scanf("%d", & n)
        for (int i=1
             i <= n
             i++) {
            scanf("%d", & a[i])
        }
        printf("%d\n", go(1, n))
    }
    return 0
}
'''
