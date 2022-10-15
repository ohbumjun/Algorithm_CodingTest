// https://www.acmicpc.net/problem/17404


#include<iostream>
#include<algorithm>
#include<limits.h>

using namespace std;

int n;
int rgb[1001][3];
int dp[1001][3];

// 깊이, 이전 색, 시작 색
int dfs(int depth, int pre, int start) {

	if (depth == n) return 0;

	if (dp[depth][pre] != -1) return dp[depth][pre];

	int result = INT_MAX;

	for (int i = 0; i < 3; i++) {
		if (depth == n - 1) { // 추가된 조건 처리!
			if (i != pre && i != start) {
				result = min(result, rgb[depth][i] + dfs(depth + 1, i, start));
			}
			else continue;
		}
		else {

			if (i != pre) {
				result = min(result, rgb[depth][i] + dfs(depth + 1, i, start));
			}
		}
	}
	
	// 이전 색칠 값의 정보를 저장하여 중복 연산을 방지한다.
	dp[depth][pre] = result;
	
	return result;
}


int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int k = 0; k < 3; k++) {
			cin >> rgb[i][k];
			dp[i][k] = -1;
		}
	}
	int result = INT_MAX;

	for (int i = 0; i < 3; i++) { // 1번 집의 색을 나타냄
    
		for (int i = 0; i < n; i++) {
			for (int k = 0; k < 3; k++) {
				dp[i][k] = -1;
			}
		}

		int temp = dfs(1, i, i) + rgb[0][i];
		result = result > temp ? temp : result;
	}

	cout << result;
}