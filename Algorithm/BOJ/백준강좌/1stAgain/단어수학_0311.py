# https://www.acmicpc.net/problem/1339

'''
결국, 알파벳에 들어갈 숫자들을 구하는 것이다

여기서 중요한 조건은, 
알파벳의 개수 <= 10 이라는 것이다.

최대값을 구하는 것이므로
알파벳의 개수만큼 
9 ~ 
를 차례대로 넣으면 된다.

예를 들어,ㅓ
GCF + ACDEF

=> G C F A D E B
9, 8, 7, 6, 5, 4, 3 를 해당 알파벳들에 넣으면 된다.

시간 복잡도 : 10! * 10 

어떻게 넣는다고 ?
순열 !
우리는 최댓값을 구하는 거야.

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
    i = len(a) - 1

    while i > 0 and a[i-1] > a[i]:
        i -= 1
    if i == 0:
        return False

    j = len(a) - 1
    while a[j] < a[i-1]:
        j -= 1

    a[j], a[i-1] = a[i-1], a[j]

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


def calc(a, letters, d):
    # alpha 에 d 관련 문자열 할당하기
    m = len(letters)
    sum = 0
    alpha = dict()
    for i in range(len(d)):
        alpha[letters[i]] = d[i]
    for i in range(len(a)):
        now = 0
        for s in a[i]:
            now = now * 10 + alpha[s]
        sum += now
    return sum


n = int(input())
# 문자 목록들을 담을 배열 ( 한줄 한줄 )
a = [''] * n
# 문자열 배열
letters = set()
# 문자열에 따른 순열목록
d = [0] * n

for i in range(n):
    a[i] = input()
    for s in a[i]:
        letters.add(s)

# d 할당
for i in range(len(letters)):
    d[i] = 9 - i

# next_permutation을 활용 > 오름차순 정렬
d.sort()

res = 0

# letter 배열 전환
letters = list(letters)

while True:
    now = calc(a, letters, d)
    res = max(now, res)
    if not next_permutation(d):
        break

print(res)
