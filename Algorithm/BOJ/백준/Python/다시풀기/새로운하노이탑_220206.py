# https://www.acmicpc.net/problem/12906
# Python --
from collections import deque

# 시작 상태
# s[i] : i번째 막대에 들어있는 원판
# ex) s[0] : 0번째, 즉, A 막대에 들어있는 원판
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

# 시작 상태
# s[i] : i번째 막대에 들어있는 원판
# ex) s[0] : 0번째, 즉, A 막대에 들어있는 원판
s = []
for i in range(3):
    temp = input().split()
    cnt = int(temp[0])
    if cnt > 0:
        s.append(temp[1])
    else:
        s.append('')

# 최종 완성 상태
final = [0, 0, 0]
for chrs in s:
    for ch in chrs:
        final[ord(ch) - ord('A')] += 1  # 각 막대에 몇개의 원판이 있어야 하는지 최종 상태 저장하기

d = {}
d[tuple(s)] = 0
q = deque()
q.append(tuple(s))
while q:
    now = q.popleft()
    # i번째 막대에서, j번째 막대로 원판 보내기
    for i in range(3):
        for j in range(3):
            if i == j:
                continue  # 같은 막대 사이에서는 이동이 필요 없다
            if len(now[i]) == 0:
                continue  # 시작 막대에 원판이 없다면
            # y는 2차원 배열 --> y[i] : i번째 막대를 의미한다
            new = list(now[:])
            new[j] += new[i][-1]
            new[i] = new[i][:-1]
            new = tuple(new)

            if new not in d:
                # 해당 막대 모양을 만들어준 적이 없다면, 추가해준다
                d[new] = d[now] + 1
                q.append(new)
ans = ['', '', '']
for i in range(3):  # 3개의 원판 및 막대에 대해서 조사한다
    # final 이라는 숫자배열로 부터, 문자열 배열을 만들어낸다
    for j in range(final[i]):
        ans[i] += chr(ord('A') + i)

print(d[tuple(ans)])


# C++
# include <iostream>
# include <map>
# include <queue>
# include <array>
'''
using namespace std
int main() {
    array < string, 3 > s // 각 막대에 대한 정보
    
    // 처음 상태 세팅 
    for (int i = 0; i < 3; i++) {
        int cnt
        cin >> cnt
        if (cnt > 0) {
            cin >> s[i]
        } else {
            s[i] = ""
        }
    }
    int cnt[3] = {0, 0, 0}
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < s[i].length(); j++) {
            cnt[s[i][j]-'A'] += 1 // 최종상태를 확인하기 위해, 각 알파벳의 개수 넣어주기 
        }
    }
    map < array < string, 3 >, int > d  // 정수형태의 정점이 아니므로, 별도의 자료형(여기서는 map)을 사용하는 것이다 
    queue < array < string, 3 >> q
    q.push(s)
    d[s] = 0

    // 모든 이동의 경우의 수 조사해주기 
    while (!q.empty()) {
        auto now = q.front()
        q.pop()
        // 각 막대를 시작점, 끝점으로 하여 이동시키는 모든 경우의 수 3*3 을 고려해준다 ( i 에서 j 로 )
        for (int i=0
             i < 3
             i++) {
            for (int j=0
                 j < 3
                 j++) {
                if (i == j) continue
                if (now[i].length() == 0) continue
                array < string, 3 > next(now)
                next[j].push_back(next[i].back())  // 제일 위에 있는 거 빼서, 옮겨주기 == 배열 상 가장 뒤에 있는 거 빼서 뒤로 넣어주기 
                next[i].pop_back()
                if (d.count(next) == 0) {
                    d[next] = d[now] + 1
                    q.push(next)
                }
            }
        }
    }
    array < string, 3 > ans
    for (int i=0
         i < 3
         i++) {
        for (int j=0
             j < cnt[i]
             j++) {
            ans[i] += (char)('A' + i)
        }
    }
    cout << d[ans] << '\n'
    return 0
}
'''
