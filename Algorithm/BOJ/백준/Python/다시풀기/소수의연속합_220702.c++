// https://www.acmicpc.net/problem/1644

#define _CRT_SECURE_NO_WARNINGS //

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

int N;
vector<int> vecNums;
vector<bool> vecIsDecimal;
// 1) 연속된 소수의 합으로 표현
// 2) 소수는 한번만 사용될 수 있다.

void Input()
{
    cin >> N;
    vecIsDecimal = vector<bool>(N+1, false);
}

void Solve()
{
    // 1. 소수 목록 모아 두기 
    // N 보다 작은 소수 목록들을 봐야 한다.
    // 자기의 sqrt 까지만 조사한다.
    vecNums.push_back(2);
    vecNums.push_back(3);

    int decNum = 2;

	for (int i = 1; i <= N / decNum; ++i)
    {
        vecIsDecimal[decNum * i] = true;
    }

    decNum = 3;
    for (int i = 1; i <= N / decNum; ++i)
    {
        vecIsDecimal[decNum * i] = true;
    }

    for (int i = 5; i <= N; ++i)
    {
        if (vecIsDecimal[i])
            continue;

        // 소수라는 의미
        decNum = i;

        for (int j = 1; j <= N / decNum; ++j)
        {
            vecIsDecimal[decNum * j] = true;
        }

        vecNums.push_back(decNum);
    }

    // for (int i = 0; i < vecNums.size(); ++i)
    // {
    //     cout << vecNums[i] << ".";
    // }

    // 2. 투포인터를 이용하여 경우의 수를 조사한다.
    int ed         = 0;
    int curSum  = 0;
    int answer  = 0;
    int totSize   = (int)vecNums.size();

    for (int st = 0; st < totSize; ++st)
    {
	    // 계속해서 더해가다가
	    // 1) 해당 N이라는 값을 넘어가게 되면
        // - st 를 증가시키기
        // 2) 그게 아니라, N과 해당 합이 같다면 count 1 증가시키기
        while (ed < totSize)
        {
			int nxtS = curSum + vecNums[ed];

            if (nxtS == N)
            {
              // for (int i = st; i <= ed; ++i)
              //     cout << vecNums[i] << ".";
              // cout << endl;

                answer += 1;
            }

            else if (nxtS > N)
                break;

            ed += 1;

            curSum = nxtS;
        }

        curSum -= vecNums[st];
    }

    cout << answer << endl;

    return;
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