# https://www.acmicpc.net/problem/14395
'''

각 숫자를 정점
연산 한번의 과정을 간선
연산 한버는 모두 동일 --> 간선 가중치 동일
최소 연산 횟수 -->  BFS 문제

단,
10^ 9 만큼의 숫자까지 주어질 수 있다라는 점이 매우 까다로운 점이다 

이를 모두 10^ 9 다 순회하려면, 시간 오래 걸리고
bfs 를 위해서 생성하는 dist 배열도 10^9 만큼 설정해야 한다. 너무 많이 할당해야 한다 

즉, BFS로 풀수있는 문제인 줄 알았지만 ,
공간, 시간 복잡도로 인해서, BFS로 풀 수 없는 문제가 된 것이다 

------------------------------------------------------------------------------

정말  bfs 로 풀수 없는 것일까 ??
자. 우리는 사실, 최단 '경로' 를 구하는 것이지
'거리'를 구하는 것은 아니다.

여튼, 굳이 우리가 흔히 쓰는 dist라는 커다란 배열이 필요하지 
않을 수도 있다는 것이다 

그리고 4가지 연산을 보면 다음과 같다 
s + s = 2*s
s - s = 0
s / s = 1
s * s = s^2

즉, 결과적으로 우리가 연산을 해가는 과정에서 얻게 되는 결과값은

( x ^ a ) * 2 ^ b
형태가 될 수 있다는 점을 알 수 있다 

일반적으로 2^30 < 10억

즉, b는 최대 30정도가 될 수 있다는 것이고

x는 1,2 가 아니라 최소 3이라는 점에서
그냥 2^30 ~~ 10억이니까

3^b 인 b에 대해서도 30정도라고 setting 해도 될 것이다 

즉, 결과적으로 우리가 연산하면서 얻게되는 결과값들은
(x^a) * (2^b) 의 형태를 띌 것이고

a, b 도 각각 30까지만 가능하다는 점에서

총 30*30 --> 900개의 정점을 방문하게 되는 경우라고 생각해도 된다 


'''
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
아까와 비슷한 원리로 진행한다

bfs,
각 숫자들은 정점
각 숫자까지 연산하는 과정이 간선

4가지 경우 : 별도 함수 제작하기

나누기의 경우 : 0 이 아닌 경우도 만들어두기

dx = []연산 4가지 세팅해두기

단, 별도의 dist 배열을 만드는 것이 아니라
해당 숫자를 방문했는지는 check 배열로 퉁 치고

방문 경로를 담는 queue 정도는 하나 있어야 할 것 같다 

'''
LM = 1000000000
st, ed = map(int, input().split())
check = set()

check.add(st)
queue = deque()
queue.append((st, ''))
while queue:
    q, path = queue.popleft()
    if q == ed:
        if path == '':
            path = '0'
        print(path)
        exit()
    # if 문을 놓는 순서도 매우 중요하다
    # 우리는 사전순으로 앞서 가는 것을 구하고 있다
    # 즉, * 가 맨 앞에 오는 것을 우선적으로 검사한다는 것이다
    # 그렇기 때문에 단순히 bfs 이니까 + 관련 if 문을 앞에 쓰거나 하면
    # 안된다는 것이다

    # 매 연산마다 최대 900개의 check 배열을 검사하는 것이라고 할 수 있지만, 그대로 10억보다 작기 때문에 괜찮다
    if 0 <= q * q <= LM and q*q not in check:
        check.add(q*q)
        queue.append((q*q, path+'*'))
    if 0 <= q + q <= LM and q+q not in check:
        check.add(q+q)
        queue.append((q+q, path+'+'))
    if 0 <= q - q <= LM and q-q not in check:
        check.add(q-q)
        queue.append((q-q, path+'-'))
    if q != 0 and 0 <= q//q <= LM and q//q not in check:
        check.add(q//q)
        queue.append((1, path+'/'))
print(-1)


'''
C++ 연산

#include <iostream>
#include <tuple>
#include <queue>
#include <string>
#include <set>
using namespace std;
const long long limit = 1000000000LL;
int main() {
    long long s, t;
    cin >> s >> t;
    set<long long> check; 
    queue<pair<long long,string>> q; # 만든 방법 
    q.push(make_pair(s,""));
    check.insert(s);
    while (!q.empty()) {
        long long x;
        string str;
        tie(x, str) = q.front(); q.pop();
        if (x == t) {
            if (str.length() == 0) {
                str = "0";
            }
            cout << str << '\n';
            return 0;
        }
        if (0 <= x*x && x*x <= limit && check.count(x*x) == 0) {
            q.push(make_pair(x*x, str+"*"));
            check.insert(x*x);
        }
        if (0 <= x+x && x+x <= limit && check.count(x+x) == 0) {
            q.push(make_pair(x+x, str+"+"));
            check.insert(x+x);
        }
        if (0 <= x-x && x-x <= limit && check.count(x-x) == 0) {
            q.push(make_pair(x-x, str+"-"));
            check.insert(x-x);
        }
        if (x != 0 && 0 <= x/x && x/x <= limit && check.count(x/x) == 0) {
            q.push(make_pair(x/x, str+"/"));
            check.insert(x/x);
        }
    }
    cout << -1 << '\n';
    return 0;
}

'''
