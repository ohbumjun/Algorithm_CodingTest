// https://www.acmicpc.net/problem/2457

#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <array>
#include <list>
#include <set>
#include <stack> //
#include <queue>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <bitset>
#include <cstring>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N;
vector<pair<int, int>> vecTimes;
int limitStD, limitEdD;

int calDays(int M, int D)
{
    int day = 0;
	for (int i = 1; i < M; ++i)
	{
		switch (i)
		{
        case 4 : case  6 :  case 9: case 11 :
			{
            day += 30;
			}
            break;
        case 1: case  3:  case 5: case 7: case 8 : case 10 : case 12:
	        {
	            day += 31;
	        }
			break;
		case 2 :
			{
            day += 28;
			}
        break;
		}
	}

    return day + D;
}


void Input()
{
    // 끝나는 시간을 기준으로 정렬을 해야 한다.
    cin >> N;

    vecTimes.reserve(N);

    for (int i = 0; i < N; ++i)
    {
        int stM, stD, edM, edD;
        cin >> stM >> stD >> edM >> edD;

        int stDTot = calDays(stM, stD);
        int edDTot = calDays(edM, edD);

        // 끝나는 날, 시작하는 날
        vecTimes.push_back(make_pair(stDTot, edDTot));
    }

    sort(vecTimes.begin(), vecTimes.end());

    limitStD = calDays(3, 1);
    limitEdD = calDays(11, 30);
}

void Solve()
{
    int prevEd = limitStD;
    int Answer = 0, Index = -1;

    // 3월 2일 이후로 시작하면 무조건 X
    if (vecTimes[0].first > prevEd)
    {
        cout << 0;
        exit(0);
    }

    // limitEdD 날짜까지는 꽃이 살아있어야 한다.
    // 따라서 각 꽃은 prevEd - 1 까지 살아있고, prevEd 에는 진다.
    // prevEd 가 limitEdD 보다 크다는 것은, 적어도 limitEdD 날 까지는 살아있다는 것을 의미
    while (prevEd <= limitEdD)
    {
        int nxtIdx = -1;
        int maxEnd = prevEd;
	    // 시작 시간은 prevEd 보다 작거나 같으면서
        // 끝나는 시간은 가장  늦은 꽃을 선택한다.

        for (int i = 0; i < N; ++i)
        {
            // prevEd 보다는 작거아 같아야 한다.
            // 이전 꽃이 prevEd 에는 지기 
            if (vecTimes[i].first <= prevEd)
            {
                if (vecTimes[i].second > maxEnd)
                {
                    nxtIdx = i;
                    maxEnd = vecTimes[i].second;
                }
            }
        }

        if (nxtIdx == -1)
            break;

        Answer += 1;
        prevEd = maxEnd;
        Index = nxtIdx;
    }

    // prevEd 가 limitEdD 보다 크다는 것은, 적어도 limitEdD 날 까지는 살아있다는 것을 의미
    if (prevEd <= limitEdD)
        cout << 0;
    else
        cout << Answer;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    // freopen("input_c.txt", "r", stdin); //

    Input();
    Solve();

    return 0;
}