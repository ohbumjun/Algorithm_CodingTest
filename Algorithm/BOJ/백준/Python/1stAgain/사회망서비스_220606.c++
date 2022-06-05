#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <cmath>
#include <utility>
#include <list>
#include <unordered_set>
using namespace std;

const int INF = 987654321;
int N;
vector<int> adj[1000001];
vector<int> adj2[1000001];

int cache[1000000][2];

//루트 노드가 root고, 본인 노드의 상태를 알 때 서브트리에서 필요한 얼리어댑터의 최소 수
int solve(int root, bool isEA) { 
	if (adj2[root].empty()) {
		if (isEA) return 1;
		else return 0;
	}

	int& ret = cache[root][isEA];
	if (ret != -1) return ret;
	
	if (isEA) { //본인이 얼리어답터는 자식은 아무 상태가 되어도 상관없다.
		ret = 1;
		for (int child : adj2[root]) {
			ret += min(solve(child, 0), solve(child, 1));
		}
	}
	else {
		ret = 0;
		for (int child : adj2[root]) {
			ret += solve(child, 1);
		}
	}
	return ret;
}

//단방향 그래프 생성(부모->자식)
void make_tree(int root, int parent) {
	if (parent != 0) adj2[parent].push_back(root);

	for (int next : adj[root]) {
		if (next == parent) continue;
		make_tree(next, root);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	for (int i = 1; i < N; i++) {
		int u, v;
		cin >> u >> v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	memset(cache, -1, sizeof(cache));
	make_tree(1, 0); //root가 1인 단방향 그래프(트리)를 생성한다.
	cout << min(solve(1, 0), solve(1, 1)) << '\n';
	return 0;
}