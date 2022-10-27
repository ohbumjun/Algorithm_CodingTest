// https://www.acmicpc.net/problem/10986
// 주의할점 -> 계산의 범위가 int 를 넘어갈 수 있다.

#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <array>
#include <list>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <bitset>
#include <cstring>
#include <string>

#define endl "\n"
#define MAX 1000000+1
#define INF int(1e9)

using namespace std;

int N, M;
// vecSum[i] -> (0 ~ i 인덱스까지의 합) % M///
long long vecSum[1000000+1]; // N의 최대값

// 0 ~ i 인덱스가 아니라,
// 서로 다른 Idx 사이의 범위 고려
// 즉, cnt[i] => 위에서 vecSum 원소들 중에서, i 값에 해당하는
// 원소의 개수 
long long cnt[1001]; // M의 최대값

void Input()
{
    cin >> N >> M;
}

void Solve()
{
    long long answer = 0;

    for (int i = 0; i < N; ++i)
    {
        int cInput;
        cin >> cInput;

        if (i == 0)
            vecSum[i] = cInput % M;
        else
        {
            vecSum[i] = (vecSum[i - 1] + cInput) % M;
        }

        // 1) M 으로 나뉘는 부분합 첫번째 경우 //
        // 0 ~ i Idx 까지의 부분합 고려
        if (vecSum[i] == 0)
            answer += 1;

        cnt[vecSum[i]] += 1;
    }

    // 2) M 으로 나뉘는 부분합 2번째 경우
    // (a ~ b) Idx 까지의 부분합 고려
    // For 문을 0 부터 N 까지 돌린다.
    // nC2 공식을 사용한다.
    // ex) [1,2,3,5]
    // ex) M 이 5 -> 나머지가 1 인 조합
    // [1] , [1,2,3] , [1,2,3,5] -> 3가지 중 2개를 선택하기
    // ex) [1,2,3,5] , [1] => [2,3,5] 영역을 선택하는 것과 같다.. ///
    for (int i = 0; i <= M; ++i)
    {
        answer += (cnt[i] * (cnt[i] - 1)) / 2;
    }

    cout << answer << endl;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);

    Input();
    Solve();

    return 0;
}