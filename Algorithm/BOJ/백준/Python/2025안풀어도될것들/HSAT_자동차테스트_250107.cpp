// https://softeer.ai/app/assessment/index.html?xid=350802&xsrfToken=tuWTiK2pLtP7Mge1bM2OyUTuz1MoQN71&testType=practice

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, Q;
vector<long long> cars; // 서로 다름

int main(int argc, char** argv)
{
    cin >> N >> Q;
    cars.resize(N);
    for (int n = 0; n < N; ++n)
        cin >> cars[n];

    sort(cars.begin(), cars.end());

    for (int q = 0; q < Q; ++q)
    {
        long long testQ = 0;
        cin >> testQ;
        long long answer = 0;

        // 3개 선택
        // 일단 전체 N 개 중에서 중앙값 testQ 가 있는지 판단
        // 없으면 0개
        // 그러면 그 index 를 찾고, 0 ~ index - 1 과 index + 1 ~ N 개를 곱하면 된다.
        int st = 0;
        int ed = N - 1;
        while(st <= ed)
        {
            int mid = (st + ed) / 2;
            if (cars[mid] == testQ)
            {
                long long leftCnt = mid;
                long long rightCnt = (N - 1) - mid;
                answer = leftCnt * rightCnt;
                break;
            }
            else if (cars[mid] < testQ)
                st = mid + 1;
            else
                ed = mid - 1;
        }
        cout << answer << endl;
    }

   return 0;
}