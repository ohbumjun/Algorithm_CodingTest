# https://www.acmicpc.net/problem/12869

'''
3차원 dynamic 문제 풀이
d[i][j][k] : scv의 체력이 i,j,k 일때
모두 파괴하는 최소 공격횟수 

-- 
공격할 수 있는 횟수 : 3팩토리얼 = 6가지 
ex) d[i][j][k] = d[i-9][j-3][k-1] + 1

[i-9][j-3][k-1] 같은 경우
음수가 되면 모두 0으로 처리해주면서 진행 

-- 
사실 dp 를 구현할 수 있는 방법은 총 2가지 이다.
1) top - down
2) bottom - up

bottom - up 같은 경우
idx 에 직접 접근하는 형식을 띤다

하지만, 여기서는
idx가 중간에 음수가 되는 경우가 매우 많다
예외처리를 해주어야 한다는 것이다

ex) 하나의 idx : i
에 대한 예외처리는 6개를 해주어야 하고
( 왜냐하면, 빼주는 경우의 수가 6개 )

i,j,k 라는 3가지 경우가 있기 때문에
무려 18개에 대한 예외처리를 
진행해주어야 한다

이는 너무 많기 때문에
top - down approach를 사용했다 

-- 
go(a,b,c)
함수 호출을 통해
올바른 a,b,c를 당겨오는
방식을 사용했다 

'''

# python ---
n = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:
    scv += [0]
d = [[[-1]*61 for j in range(61)] for i in range(61)]

# d[i][j][k] : scv의 체력이 i,j,k 일때
# 모두 파괴하는 최소 공격횟수


def go(i, j, k):
    if i < 0:
        return go(0, j, k)
    if j < 0:
        return go(i, 0, k)
    if k < 0:
        return go(i, j, 0)
    if i == 0 and j == 0 and k == 0:  # 3개다 모두 파괴된 경우
        return 0
    ans = d[i][j][k]
    if ans != -1:  # memoization
        return ans
    ans = 10000000
    # 모든 6가지 경우의 수에 대한 최소값 비교
    if ans > go(i-1, j-3, k-9):
        ans = go(i-1, j-3, k-9)
    if ans > go(i-1, j-9, k-3):
        ans = go(i-1, j-9, k-3)
    if ans > go(i-3, j-1, k-9):
        ans = go(i-3, j-1, k-9)
    if ans > go(i-3, j-9, k-1):
        ans = go(i-3, j-9, k-1)
    if ans > go(i-9, j-1, k-3):
        ans = go(i-9, j-1, k-3)
    if ans > go(i-9, j-3, k-1):
        ans = go(i-9, j-3, k-1)
    ans += 1
    d[i][j][k] = ans
    return d[i][j][k]


print(go(scv[0], scv[1], scv[2]))

'''
C++

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
int d[61][61][61];
int go(int i, int j, int k) {
    if (i < 0) return go(0, j, k);
    if (j < 0) return go(i, 0, k);
    if (k < 0) return go(i, j, 0);
    if (i == 0 && j == 0 && k == 0) return 0;
    int &ans = d[i][j][k];
    if (ans != -1) return ans;
    ans = 10000000;
    vector<int> p = {1, 3, 9};
    do {
        if (ans > go(i-p[0], j-p[1], k-p[2])) {
            ans = go(i-p[0], j-p[1], k-p[2]);
        }
    } while(next_permutation(p.begin(), p.end()));
    ans += 1;
    return ans;
}
int main() {
    int n;
    cin >> n;
    int scv[3] = {0,0,0};
    for (int i=0; i<n; i++) {
        cin >> scv[i];
    }
    memset(d,-1,sizeof(d));
    cout << go(scv[0], scv[1], scv[2]) << '\n';
    return 0;
}


'''
