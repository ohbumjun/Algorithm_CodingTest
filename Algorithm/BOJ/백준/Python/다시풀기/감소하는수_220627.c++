// https://www.acmicpc.net/problem/1038

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
#define MAX 1000000+1
#define INF int(1e9)

using namespace std;

int N;
int curIdx = 0;
int DP[MAX][10];
int Answer = 0;

// M : 자릿수
// Idx : 자릿수 관련 Idx
void MakeComb(int M, int Idx, unsigned long long curN, int prevN, vector<unsigned long long>& vecNums)
{
   //  cout << "curN : " << curN << endl;
   //  cout << "prevN : " << prevN << endl;
   //  cout << "Idx : " << Idx << endl;
   //  cout << "M : " << M << endl;
    if (Idx == M)
    {
   //     cout << "Input : " << curN << endl;
        vecNums.push_back(curN);
        return;
    }
    for (int num = prevN - 1; num >= 0; --num)
    {
        MakeComb(M, Idx + 1, curN * 10 + num, num, vecNums);
	}
}

// Idx : 몇번째를 찾아야 하는지
// NumC : 몇번째 자릿수인지 ex) 40.41.... => 2
// FirstN : 첫째자리 숫자 ex 40,41.... => 4
void FindNum(int Idx, int NumC, int FirstN)
{
    // 순열을 만든다.
    // 작은 숫자부터 차례대로 위로 올라가면서 조사한다.
    vector<unsigned long long> vecNums;
    vecNums.reserve(100);
    MakeComb(NumC, 1, FirstN, FirstN, vecNums);

    sort(vecNums.begin(), vecNums.end());

   // cout << "Idx : " << Idx << endl; 
   // cout << "NumC : " << NumC << endl;
   // cout << "FirstN : " << FirstN << endl;
   // cout << "vecNums Size : " << vecNums.size() << endl;
    cout << vecNums[Idx] << endl;
}


void Input()
{
    cin >> N;
}

void Solve()
{
    // 1자리 숫자 값 세팅하기
    for (int i = 0; i < 10; i++)
        DP[1][i] = 1;

    if (N < 10)
    {
        for (int i = 1; i <= N; i++)
            Answer += 1;
        cout << Answer << endl;
        exit(0);
    }

    curIdx = 9;

    // for (int i = 2; i < MAX; ++i)
    for (int i = 2; i < 11; ++i)   // 어차피 감소하는 수 => 9876543210 까지가 최대
											 // 즉, 최대 10자리수까지만 조사하면 된다.
    {
	    for (int j = 1; j < 10; ++j)
	    {
            int InitCurIdx = curIdx;

            int tmpS = 0;

		    for (int k = 0; k < j; ++k)
                tmpS += DP[i - 1][k];

            // j 숫자가 i번째 자릿수에서, 맨 처음 자리에 왔을 때
            // 해당 세트에서의 감소하는 수 
            DP[i][j] = tmpS;

            curIdx += DP[i][j];

	        if (curIdx >= N)
	        {
                // 여기서 해당 숫자를 추출하면 된다.
                // 즉, 현재 숫자로부터 N - InitCurIdx 만큼 더 간 숫자를 찾아내면 된다.
                // Idx : 몇번째를 찾아야 하는지
				// NumC : 몇번째 자릿수인지
				// firstN : 첫째 자리 숫자
                FindNum(N - InitCurIdx - 1, i, j);
                return;
	        }
	    }
    }
    cout << -1;
}


int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input_c.txt", "r", stdin);

    Input();
    Solve();

    return 0;
}