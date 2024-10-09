#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

using namespace std;

int N;

vector<int> seq;		// cnt 를 위한 vec
vector<int> values;	// 역수열 저장 vec
vector<int> answer;	// 각 숫자의 위치를 저장한 vec

struct Data
{
	char str;
	int num;

	bool operator < (const Data& b) const
	{
		return num < b.num;
	}
};

void Input()
{
	cin >> N;
	values.resize(N);
	seq.resize(N);
	answer.resize(N);

	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		values[i] = num;
	}
};

void Solve()
{
	for (int i = 0; i < N; ++i)
	{
		int curN = i + 1;
		int curNV = values[i];
		int accCnt = 0;
		int numLoc = 0;
		for (int locIdx = 0; locIdx < N; ++locIdx)
		{
			if (seq[locIdx] == 1) continue;

			if (accCnt == curNV)
			{
				numLoc = locIdx;
				break;
			}
			accCnt += 1;
		}

		seq[numLoc] = 1;
		answer[numLoc] = curN;

		for (int n : seq)
			cout << n << " ";
		cout << endl;
	}

	cout << "answer" << endl;
	for (int n : answer)
	{
		cout << n << " ";
	}
	cout << endl;
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
