# https://www.acmicpc.net/problem/17140

import sys
from collections import defaultdict

n = 3
m = 3
a = [[0] * 100 for _ in range(100)]

r, c, k = map(int, input().split())
r -= 1
c -= 1

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = temp[j]

if a[r][c] == k:
    print(0)
    sys.exit(0)

for t in range(1, 101):
    if n >= m:
        mm = m
        for i in range(n):
            d = defaultdict(int)  # 특정 key에 대한 val을 지정하지 않으면 0으로 세팅
            for j in range(n):
                if a[i][j] == 0:
                    continue
                d[a[i][j]] += 1
            v = []
            for key, val in d.items():
                v.append((val, key))
            v.sort()
            l = min(len(v), 50)
            for j in range(l):
                a[i][j*2] = v[j][1]
                a[i][j*2+1] = v[j][0]
            for j in range(l*2, 100):
                a[i][j] = 0
            if mm < len(v)*2:
                mm = len(v)*2
        m = mm
    else:
        nn = n
        for j in range(m):
            d = defaultdict(int)
            for i in range(n):
                if a[i][j] == 0:
                    continue
                d[a[i][j]] += 1
            v = []
            for key, val in d.items():
                v.append((val, key))
            v.sort()
            l = min(len(v), 50)
            for i in range(l):
                a[i*2][j] = v[i][1]
                a[i*2+1][j] = v[i][0]
            for i in range(l*2, 100):
                a[i][j] = 0
            if nn < len(v)*2:
                nn = len(v)*2
        n = nn
    if a[r][c] == k:
        print(t)
        sys.exit(0)
print(-1)


'''
C++

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int n = 3;
int m = 3;
int a[100][100];
int main() {
    int r, c, k;
    cin >> r >> c >> k;
    r -= 1;
    c -= 1;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> a[i][j];
        }
    }
    if (a[r][c] == k) {
        cout << 0 << '\n';
        return 0;
    }
    for (int t=1; t<=100; t++) {
        if (n >= m) {
            int mm = m;
            for (int i=0; i<n; i++) {
                map<int,int> d;
                for (int j=0; j<m; j++) {
                    if (a[i][j] == 0) continue;
                    d[a[i][j]] += 1;
                }
                vector<pair<int,int>> v;
                for (auto &p : d) {
                    v.push_back(make_pair(p.second, p.first));
                }
                sort(v.begin(), v.end());
                int l = min((int)v.size(), 50);
                for (int j=0; j<l; j++) {
                    a[i][j*2] = v[j].second;
                    a[i][j*2+1] = v[j].first;
                }
                for (int j=l*2; j<100; j++) {
                    a[i][j] = 0;
                }
                if (mm < (int)v.size()*2) {
                    mm = (int)v.size()*2;
                }
            }
            m = mm;
        } else {
            int nn = n;
            for (int j=0; j<m; j++) {
                map<int,int> d;
                for (int i=0; i<n; i++) {
                    if (a[i][j] == 0) continue;
                    d[a[i][j]] += 1;
                }
                vector<pair<int,int>> v;
                for (auto &p : d) {
                    v.push_back(make_pair(p.second, p.first));
                }
                sort(v.begin(), v.end());
                int l = min((int)v.size(), 50);
                for (int i=0; i<l; i++) {
                    a[i*2][j] = v[i].second;
                    a[i*2+1][j] = v[i].first;
                }
                for (int i=l*2; i<100; i++) {
                    a[i][j] = 0;
                }
                if (nn < (int)v.size()*2) {
                    nn = (int)v.size()*2;
                }
            }
            n = nn;
        }
        if (a[r][c] == k) {
            cout << t << '\n';
            return 0;
        }
    }
    cout << -1 << '\n';
    return 0;
}

'''
