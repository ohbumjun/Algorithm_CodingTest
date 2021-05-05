# https://www.acmicpc.net/problem/1339

'''
결국, 알파벳에 들어갈 숫자들을 구하는 것이다
어떤 알파벳이 ( 중복 없이 ) 어떤 숫자가 들어갈 것이냐 !!

여기서 중요한 조건은, 
알파벳의 개수 <= 10 이라는 것이다.

최대값을 구하는 것이므로
알파벳의 개수만큼 
9 ~ 
를 차례대로 넣으면 된다.

----------------------------------------------------

예를 들어,ㅓ
GCF + ACDEF

=> G C F A D E B
9, 8, 7, 6, 5, 4, 3 를 해당 알파벳들에 넣으면 된다.

즉, 9개 숫자 중에서 7개를 골라서
각각의 알파벳에 넣어주면 되는 것이다 

< 시간 복잡도 : 10! * 10 >
단, 최대값을 구하는 문제이므로, 큰수부터 차례대로 7개를 골라서 넣어주어야 한다 
다만, 어떤 알파벳에 어떤 숫자가 들어갈지는 모른다.
"정해진 숫자에서, 순서만 바꿔주기 == 순열" 이용하기 
 

그래서, 모든 문자열을 입력받을 때,
중복을 제거한 상태로, 문자열 목록들 만을 입력받아( python의 경우 , set 이용하기 )

그리고 그 문자열 목록들의 길이만큼 !
ex) 문자열이 4개

9876 이렇게 순열을 만들어두고 시작해 !

그러면 예를 들어,
a, b, c, d가 차례로 들어와서, 문자열 목록을 형성하고 있다면
9, 8, 7, 6 이렇게 할당한 다음에

입력된 문자목록들을 기준으로, 
총 합을 구해봐 ( 우리가 구해야할 답)

그런데, 생각해보면
원래 들어온 문자열 형태가
a c
b c d
일 수도 있자나

이 경우에는 a, b, c, d 에 9, 8, 7, 6 을 할당한 게
최대 합을 도출하지는 않아.

그래서, 위와 같이
> 각 문자열에 숫자 할당
> 각 문자 입력받아 더해주기
> 다 하면, 새로운 순열 조합 만들기
> whlie문 또 돌기

이 과정을 반복해서
최대값을 구하면 된다. 

'''


def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


def calc(a, letters, d):
    m = len(letters)
    ans = 0
    alpha = dict()
    for i in range(m):
        alpha[letters[i]] = d[i]
    for s in a:
        now = 0
        for x in s:
            now = now * 10 + alpha[x]
        ans += now
    return ans


n = int(input())
a = ['']*n
letters = set()
for i in range(n):
    a[i] = input()
    for s in a[i]:
        letters.add(s)
letters = list(letters)
m = len(letters)
d = [i for i in range(9, 9-m, -1)]
d.sort()
ans = 0
while True:
    now = calc(a, letters, d)
    if ans < now:
        ans = now
    if not next_permutation(d):
        break
print(ans)


'''
C++
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

# alpha['a'] : 'a' 라는 문자가 어떤 수인가 --> ex) alpha['a'] == 3 !!
# 모든 알파벳은 aski 코드 값을 지닌다. 
# ex) 소문자 : 'a' == 97 >> alpha[97]로 표현될 것이다 
# ex) 대문자 : 'A' == 65 >> alpha[65]로 표현될 것이다 
char alpha[256]; 

int calc(vector<string> &a, vector<char> &letters, vector<int> &d) {

    int m = letters.size();
    int sum = 0;

    for (int i=0; i<m; i++) {
        alpha[letters[i]] = d[i];
    }

    // alpha['A'] = 9
    // alpha['B'] = 8
    // alpha['C'] = 7
    // alpha['D'] = 6


    for (string s : a) {
        int now = 0;
        for (char x : s) {
            now = now * 10 + alpha[x]; 
        }
        sum += now;
    }

    return sum;
}

int main() {
    int n;
    cin >> n;
    vector<string> a(n);
    vector<char> letters;
    for (int i=0; i<n; i++) {
        cin >> a[i];
        for (char x : a[i]) {
            letters.push_back(x);
        }
    }
    sort(letters.begin(), letters.end());
    letters.erase(unique(letters.begin(), letters.end()), letters.end()); # 여기까지 : 단어 uniq 들 
    int m = letters.size(); # 문자 개수를 

    // 4개 문자열 >> 9 8 7 6 
    // A, B , D ,G 

    vector<int> d; # 순열을 표시하는 배열 
    for (int i=9; i>9-m; i--) {
        d.push_back(i);
    }
    sort(d.begin(), d.end()); 
    int ans = 0;

    do {
        int now = calc(a, letters, d); // a는 단어, letter는 알파벳, d는 순열 
        if (ans < now) {
            ans = now;
        }
    } while (next_permutation(d.begin(), d.end())); # 새로운 순열 만들어주기 

    cout << ans << '\n';
    return 0;
}

'''
