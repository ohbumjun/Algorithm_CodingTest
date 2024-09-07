# https://www.acmicpc.net/problem/16235

# 최초 풀이
from copy import deepcopy
import heapq as hq
import sys
from functools import reduce
from collections import deque, defaultdict
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

N, M, K = map(int, input().split())
foods = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) == 0:
                continue
            # 봄
            trees[i][j].sort()
            temp = []
            dead = []
            for k in range(len(trees[i][j])):
                if(foods[i][j] >= trees[i][j][k]):
                    # 양분줄어든다
                    foods[i][j] -= trees[i][j][k]
                    # 먹는다
                    temp.append(trees[i][j][k]+1)
                else:
                    # 그외, 양분 부족시, 즉시 죽는다
                    dead.append(trees[i][j][k])
            trees[i][j] = temp
            # 여름
            for d in dead:
                foods[i][j] += d // 2
    trees_copy = deepcopy(trees)
    # 가을
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for d in range(8):
                        ni, nj = i+dx[d], j+dy[d]
                        if 0 <= ni < N and 0 <= nj < N:
                            trees_copy[ni][nj].append(1)
            # 겨울 : 양분 추가
            foods[i][j] += A[i][j]
    trees = trees_copy

res = 0
for i in range(N):
    for j in range(N):
        res += len(trees[i][j])
print(res)


'''
최초풀이 : 시간초과 
- 왜 ? trees는 3차원 배열 --> 매 year 마다 3차원 배열을
"깊은복사" 하는 것은 시간이 오래 걸린다.

아래의 정답코드는, 3차원배열을 복사하는 것이 아니라,
특정 칸에 몇개의 나무가 추가되는지에 대한 정보를 담은
2차원 배열을 매번 만드는 과정을 통해
시간을 단축시켰다.
'''

# 정답
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[5]*n for _ in range(n)]  # 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
tree = [[[] for j in range(n)] for i in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)
for _ in range(l):
    p = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = []
            tree[i][j].sort()
            dead = 0
            for x in tree[i][j]:
                if x <= d[i][j]:
                    d[i][j] -= x  # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
                    temp.append(x+1)
                    if (x+1) % 5 == 0:  # 번식하는 나무는 나이가 5의 배수이어야 하며,
                        for k in range(8):
                            nx, ny = i+dx[k], j+dy[k]
                            if 0 <= nx < n and 0 <= ny < n:  # 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
                                p[nx][ny] += 1  # 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
                else:
                    dead += x//2
            tree[i][j] = temp
            d[i][j] += dead
            d[i][j] += a[i][j]  # 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
    for i in range(n):
        for j in range(n):
            for k in range(p[i][j]):
                tree[i][j].append(1)
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)


'''
C++

#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;
int a[10][10];
int d[10][10];
int p[10][10];
vector<int> tree[10][10];
int dx[] = {-1,-1,-1,0,0,1,1,1};
int dy[] = {-1,0,1,-1,1,-1,0,1};
int main() {
    int n, m, l;
    cin >> n >> m >> l;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> a[i][j];
            d[i][j] = 5; // 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
        }
    }
    while (m--) {
        int x, y, age;
        cin >> x >> y >> age;
        tree[x-1][y-1].push_back(age);
    }
    while (l--) {
        memset(p,0,sizeof(p));
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                vector<int> temp;
                sort(tree[i][j].begin(), tree[i][j].end()); // 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
                int dead = 0;
                for (int x : tree[i][j]) {
                    if (x <= d[i][j]) {
                        d[i][j] -= x; // 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
                        temp.push_back(x+1);
                        if ((x+1) % 5 == 0) { // 번식하는 나무는 나이가 5의 배수이어야 하며,
                            for (int k=0; k<8; k++) {
                                int nx = i+dx[k];
                                int ny = j+dy[k];
                                if (0 <= nx && nx < n && 0 <= ny && ny < n) { // 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
                                    p[nx][ny] += 1; // 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
                                }
                            }
                        }
                    } else { // 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
                        dead += x/2; // 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
                    }
                }
                tree[i][j] = temp;
                d[i][j] += dead;
                d[i][j] += a[i][j]; // 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                for (int k=0; k<p[i][j]; k++) {
                    tree[i][j].push_back(1); // 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
                }
            }
        }
    }
    int ans = 0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            ans += (int)tree[i][j].size();
        }
    }
    cout << ans << '\n';
    return 0;
}


'''
