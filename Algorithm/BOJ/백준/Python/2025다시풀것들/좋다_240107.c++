// https://www.acmicpc.net/problem/1253

// 1) 이분탐색
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <algorithm>
#include <unordered_map>

#define endl "\n"

using namespace std;

int Answer = 0;
int N;
vector<int> vecNs;
vector<tuple<int, int, int>> vecSums;
unordered_map<int, int> mapSumN;

int main() {
    ios::sync_with_stdio(false);

    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);
    
    cin >> N;

    vecNs.reserve(N);
    vecSums.resize(N * N);

    for (int i = 0; i < N; ++i)
    {
        int num;
        cin >> num;
        vecNs.push_back(num);
    }

    sort(vecNs.begin(), vecNs.end());

    for (int i = 0; i < N; ++i)
    {
        int target = vecNs[i];
        vector<int> vecCopy = vecNs;
        vecCopy.erase(vecCopy.begin() + i);

        //cout << "target : " << target << endl;
        //for (const auto& elem : vecNs)
        //    cout << elem << ",";
        //cout << endl;
        //for (const auto& elem : vecCopy)
        //    cout << elem << ",";
        //cout << endl;

        int st = 0;
        int ed = vecCopy.size() - 1;

        while (st < ed)
        {
            int sum = vecCopy[st] + vecCopy[ed];
            
            if (sum == target)
            {
                // cout << "st, ed : " << vecCopy[st] << "," << vecCopy[ed] << endl;
                // cout << "Found Target : " << target << endl;
                Answer += 1;
                break;
            }
            // 더 큰 범위를 찾아야 한다.
            if (sum < target)
                st++;
            else
                ed--;
        }
    }

    cout << Answer << endl;
    
    return 0;
}

// 2) 투포인터
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <algorithm>
#include <cassert>
using namespace std;

#define INT_MAX int(1e9)

int N;

vector<long long> values;

void Input()
{
    cin >> N;

	values.resize(N);

    for (int i = 0; i < N; i++)
    {
		cin >> values[i];
    }

    sort(values.begin(), values.end());
}

void Solve()
{
    int answer = 0;
    for (int f = 0; f < N; ++f)
    {
        long long target= values[f];
        vector<long long> valuesCopy = values;
        valuesCopy.erase(valuesCopy.begin() + f);
        int left = 0;
        int right = valuesCopy.size() - 1;

        while (left < right)
        {
            int mid = valuesCopy[right] + valuesCopy[left];
            if (mid == target)
            {
                answer += 1;
                break;
            }
            else
            {
                if (mid < target)
                    left += 1;
                else // mid > target 
                    right -= 1;
            }
        }
    }
    // 정렬
    // f + s -> s 이후부터 끝까지 이분탐색
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
