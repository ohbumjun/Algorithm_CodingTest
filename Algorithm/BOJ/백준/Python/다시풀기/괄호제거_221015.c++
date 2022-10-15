// https://www.acmicpc.net/problem/2800

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
#define MAX 100000+1
#define INF int(1e9)

using namespace std;

int dRow[] = {-1, 1, 0,0};
int dCol[] =  {0, 0, -1,1};

string Map;
vector<string> Answer;
vector<pair<int, int>> GwalHo;
set<string> Visit;
bool Select[10];
bool Express_Map[210];

void Input()
{
	cin >> Map;

	stack<int> STK;

	for (int i = 0; i < Map.length(); ++i)
	{
		if (Map[i] == '(')
			STK.push(i);
		else if (Map[i] == ')')
		{
			int P = STK.top();
			STK.pop();

			// 여는 괄호, 닫는 괄호 세트
			GwalHo.push_back(make_pair(P, i));
		}
	}
}

void DFS(int Idx, int Cnt)
{
	if (Cnt >= 1)
	{
		string S = "";

		for (int i = 0; i < Map.length(); ++i)
		{
			if (Express_Map[i])
				continue;

			S += Map[i];
		}

		if (Visit.find(S) == Visit.end())
		{
			Visit.insert(S);
			Answer.push_back(S);
		}
	}

	for (int i = Idx; i < GwalHo.size(); ++i)
	{
		if (Select[i])
			continue;

		// 해당 세트의 여는 괄호, 닫는 괄호를 방문 했다고 체크하기 
		Select[i] = true;

		// true 라는 것은, 해당 자리를 빈공간으로 채운다는 것이다.
		Express_Map[GwalHo[i].first] = true;
		Express_Map[GwalHo[i].second] = true;

		DFS(i, Cnt + 1);

		Select[i] = false;

		Express_Map[GwalHo[i].first] = false;
		Express_Map[GwalHo[i].second] = false;
	}
}

void Solve()
{
	DFS(0, 0);

	sort(Answer.begin(), Answer.end());

	for (int i = 0; i < Answer.size(); ++i)
		cout << Answer[i] << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input_c.txt", "r", stdin);

	Input();
	Solve();

	return 0;
}
