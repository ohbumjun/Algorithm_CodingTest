#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <list>
#include <set>
#include <functional>
#include <unordered_map>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N;
std::vector<int> vecNums;
std::vector<int> dpNums;
std::vector<int> answerNums;

int maxDpVal = 1;
int maxLength;

void Input()
{
    cin >> N;

    dpNums = vector<int>(N, 1);

    vecNums.reserve(N);

    for (int i = 0; i < N; ++i)
    {
        int Temp;
        cin >> Temp;
        vecNums.push_back(Temp);
    }
}

void Solve()
{
    // 1) 처음 dp 는 1로 세팅하고 skip

    // 2) maxVal 구하기 
	for (int f = 1; f < N; ++f)
	{
        int curNum = vecNums[f];
        int maxLength = 0;

        // 이전 숫자 중에서 1) 자기보다 크기가 작고 2) dp 값은 최대인 값을 구한다.
		for (int s = 0; s < f; ++s)
		{
			if (vecNums[s] < curNum && dpNums[s] > maxLength)
                maxLength = dpNums[s];
		}

        dpNums[f] = maxLength + 1;

        if (dpNums[f] > maxDpVal)
        {
            maxDpVal = dpNums[f];
        }
	}

    cout << maxDpVal << endl;

    // 3) 수열 출력하기
    for (int i = N - 1; i >= 0; --i)
    {
	    if (dpNums[i] == maxDpVal)
	    {
            answerNums.push_back(vecNums[i]);
            maxDpVal -= 1;
	    }
    }

    int Size = (int)answerNums.size();

    for (int i = Size - 1; i >= 0; --i)
    {
        cout << answerNums[i] << " ";
    }
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);

    Input(); //

    Solve();

    return 0;
}