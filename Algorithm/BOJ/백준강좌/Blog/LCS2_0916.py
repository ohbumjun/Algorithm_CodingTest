#  https://www.acmicpc.net/problem/9252

'''
   '문자열'을 구하는 문제 --

   우리가 일반적으로 이러한 '경로' 및 '문자열'을 구할 때는
   어떤 값이 '왜' 바뀌었는지를 기록해주면서 와야 한다 

    3가지 경우가 있었다 ( LCS 1 참고 )
    case_1) d[i][j] = d[i-1][j-1] + 1 --> a,b 문자열의 마지막 문자가 같을 때 
    case_2) d[i][j] = d[i][j-1] --> 다를 때, j가 더 길때 
    case_3) d[i][j] = d[i-1][j] --> 다를 때, i가 더 길때 --

    d[i][j] 는
    3가지 중 하나에 해당하게 되면서
    채워나가질 것이다 

    우리는 case_1) 의 경우에만
    LCS에 추가해당하게 되는 원리로 이해할 수 있다 

    그렇다면, d[i][j]가 case_1) 로 채워질때에만 조사하여
    그때의 문자열들을 모아 출력해주면 된다 

    각각을 1,2,3 으로 세팅하여
    v[i][j]에 넣어줄 것이다 
    
'''
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

a = input()
b = input()
n = len(a)
m = len(b)
a = " " + a
b = " " + b
d = [[0]*(m+1) for _ in range(n+1)]
v = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i] == b[j]:
            # 아래 코드의 의미
            # 현재 i,j 가 같으니, 그 이전 상황은
            # i-1,j-1 이다
            d[i][j] = d[i-1][j-1] + 1
            v[i][j] = 1
        else:
            if d[i-1][j] > d[i][j-1]:
                d[i][j] = d[i-1][j]
                v[i][j] = 2  # i가 한칸 더 길다, j는 그대로, i만 i-1로
            else:
                d[i][j] = d[i][j-1]
                v[i][j] = 3
print(d[n][m])

for s in v:
    print(s)

i = n
j = m
ans = ''
while i > 0 and j > 0:
    if v[i][j] == 1:
        ans += a[i]
        i -= 1
        j -= 1
    elif v[i][j] == 2:
        # a에 문자 하나가 더 들어있고, b에는 공백이 들어간 것
        i -= 1
        # 그런데 왜 i를 한칸 앞으로 이동시키는 것일까?
        # 실질적인 비교를 위해서라면, 공백에 해당하는 j를 앞으로 이동시켜서
        # 실제 문자로 이동시켜야 하는 것이 아닌가 ?

        # 아니지. 맨 처음에 우리가 d[i][j]를 채워주는 개념 및 과정을 생각하자
        # d[i][j] = d[i-1][j]로 해준 이유가 뭐냐면
        # 현재 a[i],b[j]가 다르고 , 그로 인해 현재 2개 문자로는 lcs가 추가안됨
        # 즉, 실제 lcs를 비교하기 위해서는, i를 한칸 앞으로 이동시킨다
        # 어치피 현재 i,j로는 lcs 변화가 없기 때문에
        # i를 한칸 이동시킨 값으로 lcs 정보를 입력하겠다는 의미

        # 우리는 지금 v[i][j]를 통해서
        # 실제 lcs 정보를 보면서, 1에 해당하는 애들을 넣고 싶은 것
        # 따라서 실제 lcs 정보가 반영되어 있는
        # v[i][j]를 추적해가기 위해서 위와 같이 j가 아니라, i를 빼주는 것
    else:
        j -= 1

'''
< 아래 코드와 동일한 의미 >
while i > 0 and j > 0 :
    # 대각선에 해당하는 경우에만, lcs에 추가
    if d[i][j] == d[i-1][j] :
        i -= 1
    elif d[i][j] == d[i][j-1] :
        j -= 1
    else:
        ans += a[i]
        i -= 1
        j -= 1
print(ans[::-1])
'''
# -----------------------------------------------------------------------------------------
'''
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int d[1001][1001];
int v[1001][1001];
int main() {
    string a,b;
    cin >> a >> b;
    int n = a.size();
    int m = b.size();
    a = " " + a;
    b = " " + b;
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            if (a[i] == b[j]) {
                d[i][j] = d[i-1][j-1] + 1;
                v[i][j] = 1;
            } else {
                if (d[i-1][j] < d[i][j-1]) {
                    d[i][j] = d[i][j-1];
                    v[i][j] = 2;
                } else {
                    d[i][j] = d[i-1][j];
                    v[i][j] = 3;
                }
            }
        }
    }
    cout << d[n][m] << '\n';
    string ans = "";
    while (n > 0 && m > 0) {
        if (v[n][m] == 1) {
            ans += a[n];
            n--; m--;
        } else if (v[n][m] == 2) {
            m--;
        } else {
            n--;
        }
    }
    reverse(ans.begin(), ans.end());
    cout << ans << '\n';
    return 0;
}

'''
