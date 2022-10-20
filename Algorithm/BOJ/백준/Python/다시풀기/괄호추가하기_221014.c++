#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <functional>
#include<queue>
#include<map>
#include <set>
#include <string>
#include <climits>

#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

int n, max_ans;
string str;

// 연산함수
int cal (int a, int b, char oper)
{
    int result = a; //

	switch (oper)
	{
	case '+' :
        result += b;
        break;
	case '-' :
        result -= b;
        break;
    case '*':
        result *= b;
        break;
    case '/':
        result /= b;
        break;
	}

    return result;
}

void recur (int idx, int cur)
{
	// 종료 조건
    if (idx > n - 1)
    {
        max_ans = max(max_ans, cur);
        return;
    }

    char oper = (idx == 0) ? '+' : str[idx - 1];

    // 괄호로 묶는다.
    if (idx + 2 < n)
    {
        int bracket = cal(str[idx] - '0', str[idx + 2] - '0', str[idx + 1]);
        recur(idx + 4, cal(cur, bracket, oper));
    }

    // 괄호로 안 묶는다.
    recur(idx + 2, cal(cur, str[idx] - '0', oper));
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);
    
    cin >> n >> str;

    max_ans = INT_MIN;

    recur(0, 0);

    cout << max_ans; ///

    return 0;
}