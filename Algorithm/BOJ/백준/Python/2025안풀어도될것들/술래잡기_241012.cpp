// https://www.codetree.ai/training-field/frequent-problems/problems/hide-and-seek?page=4&pageSize=5

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <cassert>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>
#include <sstream>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

// #define DEBUG 1

using namespace std;

int Q;
int N; // 도시 수
int M; // 간선 수

vector<vector<int>> minDistGraph;

// key : id
// value : <stCity, rev, dest>
struct Product
{
	int stCity;
	int rev;
	int dest;
};
unordered_map<int, Product> managedList;

// city, profit
vector<pair<int,int>> sellPossibles;

int currentCity = 0;

void compareSellPossible(int pId)
{
	const Product& p = managedList[pId];
	int pStCity = p.stCity;
	int pDest = p.dest;
	int distBet = minDistGraph[pStCity][pDest];

	// 갈 수 없음
	if (distBet == INT_MAX)
		return;

	int cost = distBet;
	int profit = p.rev - cost;

	// 판매 불가 상품
	if (profit < 0)
		return;

	if (sellPossibles.size() == 0)
	{
		sellPossibles.push_back({ pId, managedList[pId].rev });
	}
	else
	{
		int maxProfit = sellPossibles[0].second;

		if (profit > maxProfit)
		{
			sellPossibles.clear();
			sellPossibles.push_back({ pId, profit });
			maxProfit = profit;
		}
		else if (profit == maxProfit)
		{
			sellPossibles.push_back({ pId, profit });
		}
	}
	sort(sellPossibles.begin(), sellPossibles.end());
}

void resetSellPossibles()
{
	// cost 우선순위 정보도 모두 변경해야 할 것 같다.
	// 이것도 안되면 break
	int maxProfit = -1;
	sellPossibles.clear();
	for (auto iter = managedList.begin();
		iter != managedList.end();
		++iter)
	{
		int pId = iter->first;
		int pStCity = iter->second.stCity;
		int pDest = iter->second.dest;
		int distBet = minDistGraph[pStCity][pDest];

		if (distBet == INT_MAX)
			continue;

		int cost = distBet;
		int profit = iter->second.rev - cost;

		// < 0 으로 해야하는지는 고민해야 한다.
		if (profit < 0)
			continue;

		if (profit > maxProfit)
		{
			sellPossibles.clear();
			sellPossibles.push_back({ pId, profit });
			maxProfit = profit;
		}
		else if (profit == maxProfit)
		{
			sellPossibles.push_back({ pId, profit });
		}
	}
	sort(sellPossibles.begin(), sellPossibles.end());
}

vector<string> splitStr(string input, char deli)
{
	vector<string> answer;
	stringstream ss(input);
	string temp;

	while (getline(ss, temp, deli))
	{
		answer.push_back(temp);
	}

	return answer;
}

void calDist(int stCity, int curCity, int sum,
	vector<bool>& check)
{
	if (check[curCity])
		return;

	if (minDistGraph[stCity][curCity] != INT_MAX &&
		minDistGraph[stCity][curCity] < sum)
	{
		// 기존 연결 정보가 이미 있었는데
		// 해당 기존 정보가 더 거리가 작다면 return;
		return;
	}

	// 정보 update
	minDistGraph[stCity][curCity] = sum;

	check[curCity] = true;

	for (int nxt = 0; nxt < N; ++nxt)
	{
		// 같은 도시
		if (nxt == curCity)
			continue;
		// 연결되어 있는 정보가 아니라면
		if (minDistGraph[curCity][nxt] == INT_MAX)
			continue;
		calDist(stCity, nxt, sum + 
			minDistGraph[curCity][nxt], check);
	}

	check[curCity] = false;
}
void Input()
{
	cin >> Q;

	// 1) 코드 트리 랜드 건설
	// lie 단위로 입력받는다
	string firstCmdStr;
	getline(cin, firstCmdStr, '\n');
	getline(cin, firstCmdStr, '\n');

	vector<string> firstCmds = splitStr(firstCmdStr, ' ');

	// N = *firstCmds[1].c_str() - '0';
	N = stoi(firstCmds[1].c_str());
	// M = *firstCmds[2].c_str() - '0';
	M = stoi(firstCmds[2].c_str());

	minDistGraph.resize(N, vector<int>(N, INT_MAX));

	// 자기 자신으로의 거리는 0 으로 초기화 한다.
	for (int i = 0; i < N; ++i)
		minDistGraph[i][i] = 0;

	firstCmds.erase(firstCmds.begin() + 0);
	firstCmds.erase(firstCmds.begin() + 0);
	firstCmds.erase(firstCmds.begin() + 0);

	for (int idx = 0; idx < firstCmds.size() / 3; ++idx)
	{
		int city1  = stoi(firstCmds[idx * 3]);
		// int city1  = *firstCmds[idx * 3].c_str() - '0';
		int city2  = stoi(firstCmds[idx * 3 + 1]);
		// int city2  = *firstCmds[idx * 3 + 1].c_str() - '0';
		int weight = stoi(firstCmds[idx * 3 + 2]);
		// int weight = *firstCmds[idx * 3 + 2].c_str() - '0';

		// 방향 없는 간선
		minDistGraph[city1][city2] = min(
			minDistGraph[city1][city2], weight);
		minDistGraph[city2][city1] = min(
			minDistGraph[city2][city1], weight);
	}

	// 각 도시 사이의 최단 거리 정보를 update 해줘야 한다.
	// 알고리즘 사용 -> 이거는 시간 초과.
	// for (int k = 0; k < N; ++k)
	// {
	// 	for (int f = 0; f < N; ++f)
	// 	{
	// 		for (int s = 0; s < N; ++s)
	// 		{
	// 			if (f == k || s == k)
	// 				continue;
	// 			int FKDist = minDistGraph[f][k];
	// 			int SKDist = minDistGraph[k][s];
	// 			minDistGraph[f][s] = min(
	// 				minDistGraph[f][s], FKDist + SKDist);
	// 		}
	// 	}
	// }

	// dfs 를 통해서 각 정점까지의 거리 정보를 update 해야 한다.
	// check 배열 (1차원)
	// 거리 누적
	// 시작 st 는 계속 넘겨주기
	// 해당 거리까지의 최단 거리 정보 update 시켜주기
	for (int city = 0; city < N; ++city)
	{
		vector<bool> check(N, false);
		calDist(city, city, 0, check);
	}
}


void Solve()
{
	/*
	* N 개 도시, M 개 간선
	* - 각 도시는 0 ~ N-1 번호
	* - 간선은 방향 X
	* - 2개 도시 연결 간선 "여러개" 가능
	* - "자기 자신" 연결 간선 존재 가능
	*/

	/*
	* 출발지 : '0' 번
	* 
	* 5가지 명령
	* 
	* 1) 코드 트리 랜드 건설
	* - 도시 수 n, 간선 수 m, 가중치 w
	* 
	* 2) 여행 상품 생성 (200)
	* - id, rev, dest 여행 상품 생성,
	* - "관리 목록" 에 추가
	* - 각 고유 id, 매출 rev, 도착지 dst
	* 
	* 3) 여행 상품 취소 (300)
	* - 고유 식별자 id "존재" 할 경우, 
	* "관리 목록" 에서 삭제
	* 
	* 4) 최적 여행 상품 판매 (400)
	* - "관리 목록" 중에서 "최적 여행 상품" 판매
	* - cost : "현재" 여행 상품 "출발지" ~ id 상품 도착지 까지 "최단 거리" 
	* 
	* if. 출발 ~ dest 도달 불가 시, "판매 불가" 상품
	* cost > rev 여서 "이득" 이 없어도 "판매 불가" 상품
	* 
	* 조건
	* a) - rev - cost 가 "최대" 
	* b) a)가 동일하면, id 가 가장 작은 상품
	* 
	* 가장 높은 우선순위 "1개" 판매.
	* 해당 상품 "id" 출력
	* "관리 목록" 에서 제거
	* 
	* 만약 판매 가능 상품 0 개 ? -> '-1' 출력
	*		"관리 목록" 제거 X
	* 
	* 5) 여행 상품 출발지 변경 (500)
	* - 여행 상품 출발지를 "전부" "s" 로 변경
	* - 이에 따라 각 상품의 cost id (비용) 은 달라짐
	*/

	resetSellPossibles();

	// Q - 1 ? 맨 처음 input 받음
	for (int q = 0; q < Q - 1; ++q)
	{
		string cmdStrings;
		getline(cin, cmdStrings, '\n');
		vector<string> infos = splitStr(cmdStrings, ' ');

		if (infos.size() == 0)
			return;

		string cmdKind = infos[0];

		if (cmdKind == "200")
		{
			// *2) 여행 상품 생성(200)
			// * -id, rev, dest 여행 상품 생성,
			// * -"관리 목록" 에 추가
			// * -각 고유 id, 매출 rev, 도착지 dst
			int id	= stoi(infos[1].c_str());
			// int id	= *infos[1].c_str() - '0';
			int rev = stoi(infos[2].c_str());
			// int rev = *infos[2].c_str() - '0';
			int dest = stoi(infos[3].c_str());
			// int dest = *infos[3].c_str() - '0';

			managedList[id] = { currentCity, rev, dest };

			compareSellPossible(id);
		}
		else if (cmdKind == "300")
		{
			// *3) 여행 상품 취소(300)
			// * -고유 식별자 id "존재" 할 경우,
			// * "관리 목록" 에서 삭제
			int id = stoi(infos[1].c_str());
			// int id = *infos[1].c_str() - '0';

			managedList.erase(id);
		}
		else if (cmdKind == "400")
		{
			// *4) 최적 여행 상품 판매(400)
			// * -"관리 목록" 중에서 "최적 여행 상품" 판매
			// * -cost : "현재" 여행 상품 "출발지" ~
			//			id 상품 도착지 까지 "최단 거리"
			// *if.출발 ~dest 도달 불가 시, "판매 불가" 상품
			// * cost > rev 여서 "이득" 이 없어도 "판매 불가" 상품
			// *
			// *조건
			// * a) - rev - cost 가 "최대"
			// * b) a)가 동일하면, id 가 가장 작은 상품
			// *
			// * 가장 높은 우선순위 "1개" 판매.
			// * 해당 상품 "id" 출력
			// * "관리 목록" 에서 제거
			// *
			// *만약 판매 가능 상품 0 개 ? -> '-1' 출력
			// * "관리 목록" 제거 X
			
			if (sellPossibles.size() == 0)
			{
				cout << -1 << endl;
			}
			else
			{
				const pair<int,int>& sellPIdInfo = sellPossibles[0];
				cout << sellPIdInfo.first << endl;;
				managedList.erase(sellPIdInfo.first);
				sellPossibles.erase(
					sellPossibles.begin()
				);
			}
		}
		else if (cmdKind == "500")
		{
			// *5) 여행 상품 출발지 변경(500)
			// * -여행 상품 출발지를 "전부" "s" 로 변경
			// * -이에 따라 각 상품의 cost id(비용) 은 달라짐

			// int s = *infos[1].c_str() - '0';
			int s = stoi(infos[1].c_str());

			for (auto iter = managedList.begin();
				iter != managedList.end();
				++iter)
			{
				int pId = iter->first;
				managedList[pId].stCity = s;
			}

			currentCity = s;

			resetSellPossibles();
		}
	}
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


