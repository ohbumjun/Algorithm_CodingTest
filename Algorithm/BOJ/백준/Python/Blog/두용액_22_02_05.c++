#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

int N;
std::vector<int> water;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    cin >> N;
    water.reserve(N);

    int input;
    for (int i = 0; i < N; i++)
    {
        cin >> input;
        water.push_back(input);
    }

    std::sort(water.begin(), water.end());

    int Left = 0, Right = N - 1;

    int Min = abs(water[Left] + water[N-1]);
    int MinLeft = water[Left], MinRight = water[N - 1];

    // 둘다 0번째 Idx 에서 시작하기
    // 만약 절대값이 현재 최소보다 크거나 같다면, End를 증가
    // 만약 절대값이 현재 최소보다 작다면, count 하고, start 증가 ( 더 작은 값이 있는지 )

    while (Left < Right && Right < N)
    {
        // cout << "Left : " << Left << ". Right : " << Right << endl;
        // cout << "water[Left] : " << water[Left] << ". water[Right] : " << water[Right] << endl;
        int Temp      = water[Left] + water[Right];
        int AbsTemp = abs(water[Left] + water[Right]);
        // cout << "Temp : " << Temp << ", AbsTemp : " << AbsTemp << ", Min : " << Min << endl;
    	// cout << endl;
        if (AbsTemp < Min)
        {
            Min = AbsTemp;
            MinLeft = water[Left], MinRight = water[Right];
        }
        if (Temp <= 0) // 0보다 작거나 같아도 0에 가까워녀야 한다.
        {
            Left += 1;
        }
        else // 0보다 크면, 0에 가까워져야 한다.
        {
            Right -= 1;
        }
    }
  
    cout << MinLeft << " " << MinRight;

    return 0;
}


