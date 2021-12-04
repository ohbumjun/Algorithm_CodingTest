# https://www.acmicpc.net/status?user_id=dhsys112&problem_id=5557&from_mine=1

# bottom-up : 가는 방향 고려
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
n개의 숫자가 있다고 한다면
등식을 넣을 수 있는 자릿수는 n-1개 가 될 것이다

하지만, 마지막에는 '등호 ='를 넣는다고 했기 때문에
실제 +,- 를 넣을 수 있는 곳의 개수는
n - 2 개가 된다

따라서, 총 경우의 수는 2 ^ (n-2) 개가 있는 것이다 
하지만, n기 100개,
2 ^ 98까지를 모두 고려해야 한다는 점에서
시간초과를 고려할 수 밖에 없다

-------------------------------------------------

문제의 조건을 고려해보자
1) 음수 x
2) 20을 넘으면 안된다

사실, 기타리스트 문제와 거의 동일하다
그저 방법만 달라졌을 뿐이다 

'''
n = int(input())
nums = list(map(int, input().split()))
fNum = nums[len(nums)-1]
# dp[i][j] : i번째 등식까지 j 숫자를 만드는 방법의 수
dp = [[0]*21 for _ in range(n+1)]
dp[0][nums[0]] = 1

for i in range(n-1):
    for j in range(21):
        if dp[i][j] == 0:
            continue
        if j + nums[i+1] <= 20:
            dp[i+1][j + nums[i+1]] += dp[i][j]
        if j - nums[i+1] >= 0:
            dp[i+1][j - nums[i+1]] += dp[i][j]

print(dp[n-2][fNum])

# bottom up : 오는 방향 고려
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
n개의 숫자가 있다고 한다면
등식을 넣을 수 있는 자릿수는 n-1개 가 될 것이다

하지만, 마지막에는 '등호 ='를 넣는다고 했기 때문에
실제 +,- 를 넣을 수 있는 곳의 개수는
n - 2 개가 된다

따라서, 총 경우의 수는 2 ^ (n-2) 개가 있는 것이다 
하지만, n기 100개,
2 ^ 98까지를 모두 고려해야 한다는 점에서
시간초과를 고려할 수 밖에 없다

-------------------------------------------------

문제의 조건을 고려해보자
1) 음수 x
2) 20을 넘으면 안된다

사실, 기타리스트 문제와 거의 동일하다
그저 방법만 달라졌을 뿐이다 

'''
n = int(input()) - 1  # 어차피 마지막 등식은 부호, 맨 마지막 그 앞의 숫자까지 고려
nums = list(map(int, input().split()))
fNum = nums[len(nums)-1]
nums = nums[:-1]
# dp[i][j] : i번째 등식까지 j 숫자를 만드는 방법의 수
dp = [[0]*21 for _ in range(n+1)]
dp[0][nums[0]] = 1

for i in range(1, n):
    for j in range(21):
        # 0번째부터 마지막 번째까지의 숫자를 차근차근 더해가서
        # 마지막 목표 숫자를 만드는 경우의 수들이 존재할 수 있다
        # num[i]를 더해서 현재 j를 만들기 위해서는
        # 이전 i-1 번째까지의 숫자에서 nums[i]를 더한 경우를 고려하면 된다
        if j + nums[i] <= 20:
            dp[i][j] += dp[i-1][j+nums[i]]
        # 아래의 경우는, 위의 과정을 반대로 생각하면 된다
        if j - nums[i] >= 0:
            dp[i][j] += dp[i-1][j-nums[i]]

print(dp[n-1][fNum])


'''
C++

#include <iostream>
#include <vector>
using namespace std;
long long d[100][21];
int main() {
    int n;
    cin >> n;
    n -= 1;
    vector<int> a(n);
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    int goal;
    cin >> goal;
    d[0][a[0]] = 1;
    for (int i=1; i<n; i++) {
        for (int j=0; j<=20; j++) {
            if (j-a[i] >= 0) {
                d[i][j] += d[i-1][j-a[i]];
            }
            if (j+a[i] <= 20) {
                d[i][j] += d[i-1][j+a[i]];
            }
        }
    }
    cout << d[n-1][goal] << '\n';
    return 0;
}

'''
