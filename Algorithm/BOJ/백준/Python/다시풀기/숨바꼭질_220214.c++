#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <stack>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 100000 + 1
#define INF int(1e9)

using namespace std;

int N, M, K;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    freopen("input_C.txt", "r", stdin);

    int T;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        // 입력 세팅 
        cin >> N;
        cin >> M;
        cin >> K;

        std::vector<int> vecHouse;
        int House = 0;
        int Ans = 0;

        vecHouse.resize(N);

        for (int h = 0; h < N; h++)
        {
            cin >> House;
            vecHouse[h] = House;
        }

        // 원소 개수가 딱 3개라면, --> 1가지만 조사하면 된다.
        if (N == M)
        {
            int Sum = 0;

            for (int j = 0; j < M; j++)
            {
                Sum += vecHouse[j];
            }

            if (Sum < K)
                Ans += 1;
            cout << Ans << endl;
        }
        else
        {
            // 경우의 수  조사
			// 1) 맨 처음 경우 조사하기
            int Sum = 0;
            for (int k = 0; k < M; k++)
            {
                Sum += vecHouse[(k) % N];
            }

            if (Sum < K)
                Ans += 1;

            // 이후에는 앞에꺼 하나 빼고, 뒤에꺼 하나 더하고
            for (int st = 1; st <= N - 1; st++)
            {
                Sum -= vecHouse[st - 1];
                Sum += vecHouse[(st + M - 1) % N];

                if (Sum >= K)
                    continue;

                Ans += 1;
            }

            cout << Ans << endl;
        }
    }
    return 0;
}


