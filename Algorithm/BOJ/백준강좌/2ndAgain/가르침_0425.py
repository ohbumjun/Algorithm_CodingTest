# 첫번째 풀이 : 재귀 ----------------------------------------------------

'''
N개의 단어
최대 15의 단어 길이
알파벳 26 이하

이 문제는

1) 
26개의 알파벳 중에서
k개를 고르고
2) 
N개의 단어 중에서
고른 알파벳으로 이루어진 단어의 개수 

자. 1) 의 경우에 대해서는 '시간 문제상', '비트 마스크'를 적용할 수 없다.
'비트 마스크'는 보통, N 개라는 집합에 대해서, 
모든 부분 집합을 구할 때 사용한다. 

그러면 원리상으로는
0 ~ 26 중에서 , 
1 이 k개 인 것을 찾아야한다.

그러면 0 ~  2 ^ 26 까지를 계산해야 하는데,
이는 너무 큰 수이므로 안된다. 

그러므로, 이부분은 '재귀함수'를 이용한다.
how ? 해당 알파벳을 고를지 안고를지를 판단해가면서
k개를 고를때까지 반복하면 되는 것이다.
그런데 이것도 사실 결국은 2 ^ 26 이다.

뿐만 아니라,
이렇게 2 ^ 26개의 경우의 수가 나오는 1) 에 대햇

2) 도 일일히 다 해줘야 한다.
시간 초과가 날 수 밖에 없는 것이다.

그런데, 조건이 있다
모든 단어는 anta로 시작, tica로 끝난다
즉, 다시 말하면, 
a n t i c라는 글자는 무조건 포함해야 한다는 것이다.

"결과적으로 우리는 25 - 5 개 글자 중에서 K - 5개를 선택하는 경우의 수로 좁혀든다. "

2) 에서의 시간 복잡도는 ?
N개의 단어에 대해, 알파벳 각각을 조사해야 한다.
단어의 길이를 L이라고 한다면
O ( N * L) 이 되는 것이다.
( N은 최대 50, L은 최대 15 )


'''


# 첫번째 풀이 : 시간 초과
from random import randrange, randint
import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
문제의 원리 : 26개의 알파벳 중에서
n개의 알파벳을 뽑고 ,

그렇게 뽑은 알파벳들을 기준으로 해서
N개의 단어중 읽을 수 있는
단어의 개수 구하기

'''
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

# 알파벳 선택함수


def go(index, k, words):
    # index : 알파벳
    # k : 남아있는 ( 즉, 반대로 생각하면, 지금까지 선택한 알파벳의 개수를 미루어 알 수 있다 ) > K개의 글자로만 이루어진 단어의 개수를 고르는 문제
    # k가 음수가 되버리면, 애초부터 불가능, 더이상 선택할 수 없는 알파벳의 개수가 없는 경우는 괜찮다. 이후 알파벳들은 사용하지 않는 방향의 경우의 수를 구하면 되기 때문
    ans = 0
    if k < 0:
        return 0  # 왜 0을 리턴해주는 것일까?
    if index == 26:
        return count(words)

    # 해당 요소를 선택하기
    letters[index] = 1
    t1 = go(index + 1, k - 1, words)
    ans = max(ans, t1)

    # 해당 요소를 선택하지 않기
    letters[index] = 0

    if index != ord('a') - ord('a') and index != ord('c') - ord('a') and index != ord('n') - ord('a') and index != ord('t') - ord('a') and index != ord('i') - ord('a'):
        t2 = go(index + 1, k, words)
        ans = max(ans, t2)
    return ans

    # 위 함수에서의 시간 복잡도는 O(2 ^ 26)처럼 보이지만, O ( 2 ^ 21 ) 이다
    # 왜냐하면, a, t, n, c, i에 대해서는, 선택하는 경우에 대해서만 고려했기 때문이


# count 함수
def count(words):
    cnt = 0
    for word in words:
        ok = True
        for a in word:
            if letters[ord(a) - ord('a')] == 0:
                ok = False
                break
        if ok == True:
            cnt += 1
    return cnt


n, s = map(int, input().split())
arr = [list(input()) for _ in range(n)]
cnt = 0
letters = [0] * 26
print(go(0, s, learn))

# 시간 복잡도 ?
'''
알파벳 고르기 : O( 2 ^ 21 )

고른 각각의 알파벳 세트에 대해서, 
읽을 수 있는 단어의 수 세기 : O( 50 * 20  ) 

15억 : 시간초과
'''

# 두번째 풀이 : 비트 마스크 ----------------------------------------------

'''
위의 과정은 다음과 같다
1) 26 - 5개 알파벳 중에서 k - 5개를 고름
2) 각각의 단어에 대해서
3) 해당 단어의 각 문자가, 우리가 고른건지 확인 

= O( 2 ^ 21 * N * L )

위의 과정에서 시간을 어디서 줄일 수 있을까?
3) 번 !

'비트마스크'를 통해 줄인다.
HOW ?

예를 들어, 
' a c d '를 배웠다고 할때

단어 1 : ac
단어 2 : acaac 
단어 3 : ca
단어 4 : caaaac

모두 읽을 수 있다.
여기서 배울 수 있는 점은 무엇일까 ? 

1)  단어 내에서 알파벳의 숫자는 의미없다
- 그저 내가 읽은 단어에 , 해당 알파벳이 있기만 하면 되는거니까
- 순서 다른 것은 의미 없다
2) 구성만 같으면 되고, 어떤 알파벳의 개수는 의미가 없다.
- 즉, 위의 단어4개는, 우리 눈에는 단어 4개가 다르게 보이지만,

문제 입장에서는, 배웠다.배우지 않았다
2개로 분리된다는 것이다.


< 해결책 >
단어를 저장할 때, 
단어를 저장하는 것이 아니라,
단어에 속해있는 알파벳이 무엇인지를 저장할 것이다.

a : 0
b : 1
..
..
z : 25 번째 알파벳 

우리는 해당 단어가 있는지 없는지만 검사하면 되기 때문에
bit mask를 사용하게 된다 

위의 단어 4개는 모두 a , c로만 이루어져 있기 때문에

101 (2) = 5
따라서 5로 저장하면 된다.

< 예시 : 편의상 a,b,c,d >
배움 L : 1101(2) = { a,c,d }
단어 1 : a, b = 0011(2)

우리는 단 한번의 연산으로
단어 1에 , 우리가 배우지 않은 알파벳이 포함되어 있는지 없는지를 알 수 있다

즉, 우리가 해야할 일은,
단어에 배우지 않은 알파벳이 있는지, 없는지 검사하는 것 

그렇다면, 배우지 않은 알파벳을 만들어줘야 한다.

즉, 배운 단어가 L이라면
배우지 않은 단어는 ~L 이라고 해야 한다.

우리는 결국 단어에 
배우지 않은 알파벳이 있는지를 검사해야 한다.

단어 & ~L = 1 이어야 한다.

즉, 어떤 단어가 있는데, 해당 단어를 배우지 않았다면 ( ~L == 1) 
그 비트연산의 결과는 1이 될 것이다.

즉, 단어에 배우지 않은 단어가 '없다면' 
단어 & ~L == 0 이 될 것이다.

비트 연산의 시간 복잡도는 1이다.
결국 앞에서 '특정 단어의 각 문자가 고른 문자에 포함되어 있는가' 에 대한
시간 복잡도를 O(L)에서 O(1)로 줄일 수 있는 것이다.

비트연산을 할 때 주의할 점이 있다
L = 1101(2)일 때
~L = 0010(2) 이 아니다 !!

보통은 해당 bitmask에서 int를 사용하고 , 
c++, java, python의 경우 일반적으로 32bit 정수를 의미한다.

즉, 1101 이 실제 저장될 때에는
0000000000000000000000000000000000001101
이와 같이 0이 앞에 쭉 있고, 28개를 채운 다음 
1101 이 나온다는 것이다.

이 상태에서 비트에다가 not연산을 하게 되면
111111111111111111111111111111111110010 
이렇게 된다

우리는 맨 뒤 4자리
1101을
0010 
으로 바꾸고 싶은 것이다.

어떻게 ??

ex) 
 1111
-1101
------
 0010

즉, 1111 에서 해당 숫자를 빼면, 반전되는 것이다.

1111은 ( 1<<4) - 1 이다. 


즉, 우리는 4글자가 아니라 26글자의 알파벳을 다루고 있기 때문에 
( 1 << 26 ) - 1 -L  이
우리에게 필요한 Not 연산이 되는 것이다.

'''
sys.setrecursionlimit(100000)


def count(mask, words):
    cnt = 0
    for word in words:
        if word & ((1 << 26) - 1 - mask) == 0:
            cnt += 1
    return cnt


def go(idx, k, mask, words):
    if k < 0:
        return 0
    if idx == 26:
        return count(mask, words)
    # 해당 값을 선택했을 때, mask에 해당 bit mask형태를 더해간다
    ans = 0
    t1 = go(idx + 1, k - 1, mask | 1 << idx, words)
    ans = max(ans, t1)

    if idx not in [ord('a')-ord('a'), ord('c')-ord('a'), ord('t') - ord('a'), ord('i')-ord('a'), ord('n') - ord('a')]:
        t2 = go(idx + 1, k, mask, words)
        ans = max(ans, t2)

    return ans


n, k = map(int, input().split())
words = [0] * n

for i in range(n):
    word = sys.stdin.readline()[:-1]
    for a in word:
        # |= : 비트마스크 관점에서, 계속 값을 추가해가는 것이
        # 예를 들어, 'abcd' 라고 한다면
        # 0001
        # 0011
        # 0111
        # 1111
        # 이와 같은 과정으로 추가되어 간다는 것이다
        words[i] |= 1 << (ord(a) - ord('a'))

print(go(0, k, 0, words))

'''
#include <iostream>
#include <vector>
#include <string>
using namespace std;
int count(int mask, vector<int> &words) {
    int cnt = 0;
    for (int word : words) {
        if ((word & ((1<<26)-1-mask)) == 0) {
            cnt += 1;
        }
    }
    return cnt;
}
int go(int index, int k, int mask, vector<int> &words) {
    if (k < 0) return 0;
    if (index == 26) {
        return count(mask, words);
    }
    int ans = 0;
    int t1 = go(index+1, k-1, mask | (1 << index), words);
    if (ans < t1) ans = t1;
    if (index != 'a'-'a' && index != 'n'-'a' && index != 't'-'a' && index != 'i'-'a' && index != 'c'-'a') {
        t1 = go(index+1, k, mask, words);
        if (ans < t1) ans = t1;
    }
    return ans;
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<int> words(n);
    for (int i=0; i<n; i++) {
        string s;
        cin >> s;
        for (char x : s) {
            words[i] |= (1 << (x-'a'));
        }
    }
    cout << go(0, m, 0, words) << '\n';
    return 0;
}

'''
