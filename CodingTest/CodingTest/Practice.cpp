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

int V, E; // 정점 개수, 간선 개수
int K; // 시작 번호
vector<vector<pair<int, int>>> vecGraph;

void Input()
{
	cin >> V >> E;
	cin >> K;

	vecGraph.resize(V + 1);

	int st, ed, cst;

	for (int i = 0; i < E; ++i)
	{
		cin >> st >> ed >> cst;
		vecGraph[st].push_back(make_pair(ed, cst));
	}
}

void Solve()
{
	// 각 정점까지의 최단 거리 정보
	vector<int> vecMinD = vector<int>(V + 1, INF);

	// 거리, 정점
	// 내림차순 (큰거 -> 작은거)
	priority_queue<pair<int, int>> Queue;

	// 거리 정보 -1로 세팅해서 점검했다는 것 확인하기
	vecMinD[K] = 0;

	Queue.push(make_pair(0, K));

	while (!Queue.empty())
	{
		pair<int, int> curInfo = Queue.top();
		Queue.pop();

		// cout << "Bef Queue Size : " << Queue.size() << endl;

		// 거리 정보 비교
		int curDist = -curInfo.first;
		int curVtx = curInfo.second;

		if (vecMinD[curVtx] < curDist)
			continue;

		// cout << "curVtx, curDist : " << curVtx << "," << curDist << endl;

		// 업데이트 한 정점을 기준으로 또 다시 최단 거리 정보 Update
		for (int i = 0; i < vecGraph[curVtx].size(); ++i)
		{
			int nxtVtx = vecGraph[curVtx][i].first;
			int nxtDst = curDist + vecGraph[curVtx][i].second;

			if (vecMinD[nxtVtx] > nxtDst)
			{
				// cout << "nxtVtx, bef nxtDst, aft Dist : " << nxtVtx << "," << vecMinD[nxtVtx] << "," << curDist + nxtDst << endl;
				vecMinD[nxtVtx] = nxtDst;
				Queue.push(make_pair(-nxtDst, nxtVtx));
			}
		}

		// cout << "Aft Queue Size : " << Queue.size() << endl;
		// for (int i = 1; i <= V; ++i)
		//   	cout << vecMinD[i] << ".";
		// cout << endl;
		// cout << endl;
	}

	for (int i = 1; i <= V; ++i)
	{
		if (i == K)
			cout << 0 << endl;
		else if (vecMinD[i] == INF)
			cout << "INF" << endl;
		else
			cout << vecMinD[i] << endl;
	}
}
int main()
{
	ios::sync_with_stdio(false);

	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input.txt", "r", stdin);

	Input();

	Solve();
}

/*
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

int V, E; // 정점 개수, 간선 개수
int K; // 시작 번호
vector<vector<pair<int, int>>> vecGraph;

void Input()
{
	cin >> V >> E;
	cin >> K;

	vecGraph.resize(V+1);

	int st, ed, cst;

	for (int i = 0; i < E; ++i)
	{
		cin >> st >> ed >> cst;
		vecGraph[st].push_back(make_pair(ed, cst));
	}
}

void Solve()
{
	// 각 정점까지의 최단 거리 정보
	vector<int> vecMinD     = vector<int>(V+1, INF);

	// 거리, 정점
	// 내림차순 (큰거 -> 작은거)
	priority_queue<pair<int, int>> Queue;

	// 거리 정보 -1로 세팅해서 점검했다는 것 확인하기
	vecMinD[K] = 0;

	Queue.push(make_pair(0, K));

	while (!Queue.empty())
	{
		pair<int, int> curInfo = Queue.top();
		Queue.pop();

		// cout << "Bef Queue Size : " << Queue.size() << endl;

		// 거리 정보 비교
		int curDist = -curInfo.first;
		int curVtx = curInfo.second;

		if (vecMinD[curVtx] < curDist)
			continue;

		// cout << "curVtx, curDist : " << curVtx << "," << curDist << endl;

		// 업데이트 한 정점을 기준으로 또 다시 최단 거리 정보 Update
		for (int i = 0; i < vecGraph[curVtx].size(); ++i)
		{
			int nxtVtx = vecGraph[curVtx][i].first;
			int nxtDst = curDist + vecGraph[curVtx][i].second;

			if (vecMinD[nxtVtx] > nxtDst)
			{
				// cout << "nxtVtx, bef nxtDst, aft Dist : " << nxtVtx << "," << vecMinD[nxtVtx] << "," << curDist + nxtDst << endl;
				vecMinD[nxtVtx] = nxtDst;
				Queue.push(make_pair(-nxtDst, nxtVtx));
			}
		}

		// cout << "Aft Queue Size : " << Queue.size() << endl;
		// for (int i = 1; i <= V; ++i)
		//   	cout << vecMinD[i] << ".";
		// cout << endl;
		// cout << endl;
	}

	for (int i = 1; i <= V; ++i)
	{
		if (i == K)
			cout << 0 << endl;
		else if (vecMinD[i] == INF)
			cout << "INF" << endl;
		else
			cout << vecMinD[i] << endl;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// freopen("input_c.txt", "r", stdin);

	Input();
	Solve();

	return 0;
}
*/