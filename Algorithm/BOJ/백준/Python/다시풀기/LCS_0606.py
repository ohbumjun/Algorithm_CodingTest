# https://www.acmicpc.net/problem/9251
# LCS : Longest Common Subsequence
'''
Subsequence 
- 순서 유지하되, 연속일 필요는 없음 ( not contiguous )

Substring 
- 순서 유지 + 연속

A = 'ACAYKP'
B = 'CAPCAK'
LCS(A,B) = 'ACAK'

---------------------------------

우리는 이 문자를 아래와 같이 바라볼 수 있다
각각의 문자열에 '공백'을 삽입하여,

같은 문자가, 같은 위치에 오도록 하는 원리로 해석할 수 있다

A = ' A CAYKP'
B = 'CAPCA K '

---------------------------------

위와 같은 원리에 기초할 때, 
A = [   i]
B = [   j]

1) 각각 i-1, j-1 까지는 어떻게 되었고
2) 현재 i,j 는 어떻게 되었는가.
의 관점에서 해석할 수 있다 

---------------------------------

d[i][j] : A가 i번째 까지, B가 j번째 까지 있을 때의 , LCS 의 길이 

가능한 상황은 총 3가지가 존재한다 

< 첫번째 경우 : i번째, j번째 요소가 일치하는 경우 >  ----------------------------
A = [   i]
B = [   j]

즉, A[i] == B[j] 인 경우에 해당한다.
이는, LCS의 길이가 1 늘어나는 경우

즉, 이전 A[i-1] , B[i-1] 까지의 LCS 길이 + 1

"d[i][j] = d[i-1][j-1] + 1"

< 두번째 경우 : i번째, j번째 요소가 일치하지 않는 경우 => i가 더 뒤에 위치한 경우 >  ----------------------------
A = [     ....i]
B = [   j][공백]

A[i] != B[j]
즉, 어차피 현재 각각 한원소를 추가한다고 한들, LCS 길이는 변하지 않는다

여기의 경우, A의 i-1번째 까지, B의 j번째 까지의 LCS 길이가 유지된다
"d[i][j] =  d[i-1][j] + 0"

< 세번째 경우 : i번째, j번째 요소가 일치하지 않는 경우 => j가 더 뒤에 위치한 경우 >  ----------------------------
A = [   i][공백] 
B = [     ....j]

A[i] != B[j]
즉, 어차피 현재 각각 한원소를 추가한다고 한들, LCS 길이는 변하지 않는다

여기의 경우, A의 i번째 까지, B의 j-1번째 까지의 LCS 길이가 유지된다
"d[i][j] =  d[i][j-1] + 0"

'''

a = input()
b = input()
n = len(a)
m = len(b)
a = " " + a  # 각각 앞에 공백을 삽입해서, 아래 for문에서 idx를 1부터 시작할 수 있게 바꿔주었다
b = " " + b  # 왜 ?? 식의 과정에서 i-1, j-1 이라는 식이 들어가기 때문이다
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        # 사실, 공백을 넣어가는 과정이라고 하면 막연하게 들릴 수도 있다
        # 하지만, 여기에서 말하고자 하는 것은, i가 1이고, m이 1에서 계속 증가하는 형태라고 한다면
        # a 는 1개의 글자
        # b 는 2,3,4 ... 이렇게 글자수가 늘어난다는 것이고
        # 해당 a,b를 비교할 때, a는 b보다 글자수가 작고, 그 작은 만큼의 글자수를 '공백'으로 메꿔주는 개념
        # 그렇게 하면, 동일한 길이의 문자열 끼리, 공통 부분 문자열이 몇개인지를 구할 수 있기 때문이다
        if a[i] == b[j]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])
print(d[n][m])


'''
#include <iostream>
#include <string>
using namespace std;
int d[1001][1001];
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
            } else {
                d[i][j] = max(d[i-1][j], d[i][j-1]);
            }
        }
    }
    cout << d[n][m] << '\n';
    return 0;
}

'''
