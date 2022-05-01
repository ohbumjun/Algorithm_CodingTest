#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <list>
#include <set>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N;

unordered_map<int, vector<int>> Graph;
vector<int> People;
vector<bool> vecVisited;
vector<bool> vecIsCurrentGroup;
int Answer = INF;

void Input()
{
    cin >> N;

    // 각 구역의 사람수 정보 저장
    People.resize(N + 1);

    for (int i = 1; i <= N; ++i)
    {
        int Temp;
        cin >> Temp;
        People[i] = Temp;
    }

    // 인접 정보를 받아올 것이다.
    for (int city = 1; city <= N; ++city)
    {
        int NearNums = 0;

        cin >> NearNums;

        Graph[city].reserve(NearNums);

        int NearCity = 0;

        for (int n = 0; n < NearNums; ++n)
        {
            cin >> NearCity;
            Graph[city].push_back(NearCity);
        }
    }

    vecVisited = vector<bool>(N + 1, false);
    vecIsCurrentGroup = vector<bool>(N + 1, false);
}

void CheckConnection(int city, bool IsCurrentGroup)
{
    vecVisited[city] = true;

	for (const auto& elem : Graph[city])
	{
        if (vecVisited[elem])
            continue;

        if (vecIsCurrentGroup[elem] != IsCurrentGroup)
            continue;

        CheckConnection(elem, IsCurrentGroup);
	}
}

void CheckGroup(int num, int prevIdx, vector<int>& group)
{
	if (group.size() == num)
	{
        // 여기에서 게더링을 실시하면 된다.

        for (int i = 0; i <= N; ++i)
        {
        	// check 배열 초기화
            vecVisited[i] = false;

            // 같은 Group 여부 정보 초기화
            vecIsCurrentGroup[i] = false;
        }

        // 해당 Group 에 속한 City 들은 true 로 세팅해준다.
        for (const auto& elem : group)
        {
            vecIsCurrentGroup[elem] = true;
        }

        // 만약 Group 첫번째와 연결된 선거구 자체가 없다면 return
        // if (Graph[group[0]].size() == 0)
        //    return;

        // DFS 를 돌려서, 같은 Group 이 연결되어 있는지 체크한다.
        CheckConnection(group[0], true);

        bool Connected = true;

        for (const auto & elem : group)
        {
	        if (!vecVisited[elem])
	        {
                Connected = false;
                break;
	        }
        }

        if (!Connected)
            return;

        // 이번에는 다른 구역의 선거구들이 연결되었는지를 살펴볼 것이다.
        vector<int> otherGroup;
        otherGroup.reserve(N - group.size());

        for (int i = 1; i <= N; ++i)
        {
	        if (vecIsCurrentGroup[i] == false)
	        {
                otherGroup.push_back(i);
	        }
        }

        for (int i = 0; i <= N; ++i)
        {
            // check 배열 초기화
            vecVisited[i] = false;
        }

        CheckConnection(otherGroup[0], false);

        Connected = true;

        for (const auto& elem : otherGroup)
        {
            if (!vecVisited[elem])
            {
                Connected = false;
                break;
            }
        }

        if (!Connected)
            return;

        int GroupSum = 0;
        int OtherGroupSum = 0;

        for (int i = 1; i <= N; ++i)
        {
            if (vecIsCurrentGroup[i])
                GroupSum += People[i];
            else
                OtherGroupSum += People[i];
        }

        int TempAns = abs(OtherGroupSum - GroupSum);


        if (TempAns < Answer)
        {
            Answer = TempAns;

            // cout << "TempAns : " << TempAns << endl;
            // 
            // for (const auto& elem : group)
            // {
            //     cout << elem << ".";
            // }
            // cout << endl;
        }

        return;
	}

    for (int i = prevIdx + 1; i <= N; ++i)
    {
        group.push_back(i);
        CheckGroup(num, i, group);
        group.pop_back();
    }
}

void Solve()
{
	// 1개 ~ 반개
    int HalfNum = N / 2;

    for (int i = 1; i <= HalfNum; ++i)
    {
        vector<int> group;
        CheckGroup(i, 0, group);
    }
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input_c.txt", "r", stdin);

    Input();

    Solve();

    if (Answer == INF)
        cout << -1;
    else
        cout << Answer;

    return 0;
}