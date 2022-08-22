// https://www.acmicpc.net/problem/16562

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
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N, M, K;

vector<int> vecGraph[MAX];
vector<int> vecFCost;
vector<bool> vecCheck;

void Input()
{
	// N명의 학생

	// - 학생 I 에서 A[I] 만큼 돈을 주면, 1달간 친구가 되어준다.
	// - 친구의 친구는 친구다
	// - 가장 적은 비용으로 모든 사람과 친구가 되는 방법ㄴ

	cin >> N >> M >> K;

	for (int i = 0; i < N; ++i)
		vecGraph[i].reserve(N);
	
	vecFCost.reserve(N);

	for (int i = 0; i < N; ++i)
	{
		int Cost;
		cin >> Cost;
		vecFCost.push_back(Cost);
	}
	
	for (int i = 0; i < M; ++i)
	{
		int F;  int S;

		cin >> F >> S;

		F -= 1;S -= 1;

		vecGraph[F].push_back(S);
		vecGraph[S].push_back(F);
	}

	vecCheck = vector<bool>(N + 1, false);
}

void FindGroup(int CurF, std::vector<int>& vecF)
{
	vecF.push_back(CurF);

	for (const auto& OtherF : vecGraph[CurF])
	{
		if (vecCheck[OtherF])
			continue;

		vecCheck[OtherF] = true;

		FindGroup(OtherF, vecF);
	}
}

void Solve()
{
	// 접근 방식 : 최소 비용 신장 트리
	// 모든 친구 (정점)을 연결하는 최소 비용을 알아내야 한다.
	
	// 1. 친구 그룹들을 묶는다.
	// 2. 각 그룹에 어떤 친구들이 속하는지도 조사한다.
	// 3. 매번 어떤 친구들이 속하는지 조사할 때, 그 중 최소 비용을 구한다.
	// 4. 모든 친구 그룹들을 돌면서, 가 그룹의 최소 비용을 더한다.
	// 5. 단, 여기서 합이, K 보다 크다면, 모든 친구를 사귈 수 없다는 것이다.
	// 5. 단, 여기서 합이, K 보다 크다면, 모든 친구를 사귈 수 없다는 것이다.

	int TCost = 0;

	for (int f = 0; f < N; ++f)
	{
		if (vecCheck[f])
			continue;

		vector<int> vecF;

		FindGroup(f, vecF);

		// 최소비용조사
		int MinC = 10001;

		for (const auto& checkf : vecF)
		{
			if (vecFCost[checkf] < MinC)
				MinC = vecFCost[checkf];
		}

		TCost += MinC;
	}

	if (TCost > K)
		cout << "Oh no" << endl;
	else
		cout << TCost << endl;
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