// https://www.acmicpc.net/problem/16472

#define _CRT_SECURE_NO_WARNINGS

#include<iostream> //
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
#define MAX 1000000+1
#define INF int(1e9)

using namespace std;

int N;
int Answer = 0;
string strInput;
vector<int> vecInt;
int check[27];

void Input()
{
    cin >> N;
    cin >> strInput;
    vecInt.reserve(strInput.length());

    for (int i = 0; i < strInput.length(); ++i)
    {
        vecInt.push_back(strInput[i] - 'a');
    }
}

void Solve()
{
    int ed = 0;
    int curKinds = 1;
    check[vecInt[ed]] = 1;
    int strSize = (int)vecInt.size();

    // 현재 ed 까지 포함시키기
    // 처음에 st, ed 는 0에서 시작
    // vecInt[st] 에 해당하는 check 1 증가
    // 그 다음 지금까지 문자열 종류 개수를 의미하는 curKinds 1 증가
    // 그 다음 부터 ed 를 증가시켜나가면서
    // 1) ed + 1 에서의 문자가 0 에서 1 이 된다는 것은, curKinds 가 1 증가해야 한다는 의미
    // 그리고 vecInt[ed +1]에 해당하는 숫자 1 증가
    // 단, curKinds 는 N보다 작아야 한다.
    // 만약 이 조건을 만족하면 ed 를 계속 증가시켜 나간다
    // 2) 그게 아니라면 st 를 증가시킬 것인데
    // vecInt[st]에 해당하는 check 1 감소
    // 만약 0이 된다는 것은, curKinds 가 1 감소한다는 것을 의미한다.

   for (int st = 0; st < strSize; ++st)
   {
		while (ed + 1 < strSize)
		{
            int nxtKinds = curKinds;

            if (check[vecInt[ed + 1]] == 0)
                nxtKinds += 1;

            if (nxtKinds <= N)
            {
                ed += 1;
                check[vecInt[ed]] += 1;
                curKinds = nxtKinds;
            }
            else
                break;
		}

        Answer = max(Answer, ed - st + 1);

        check[vecInt[st]] -= 1;

        if (check[vecInt[st]] == 0)
            curKinds -= 1;
   }

    cout << Answer << endl;
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