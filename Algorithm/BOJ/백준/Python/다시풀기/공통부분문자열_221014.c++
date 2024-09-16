#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <list>
#include <set>
#include <functional>
#include <unordered_map>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int str1Len;
string str1Input;
int str2Len;
string str2Input;
vector<vector<int>> dpCommon;
vector<vector<bool>> vecIsSame;

void Input()
{
    cin >> str1Input;
    str1Len = str1Input.length();

    cin >> str2Input;
    str2Len = str2Input.length();

    dpCommon.reserve(str2Len + 1);
    vecIsSame.reserve(str2Len + 1);

    for (int i = 0; i <= str2Len; ++i)
    {
        dpCommon.push_back(vector<int>(str1Len + 1, 0));
        vecIsSame.push_back(vector<bool>(str1Len + 1, false));
    }
}

void Solve()
{
    // 먼저 같음 여부 조사하기
    for (int str2 = 1; str2 <= str2Len; ++str2)
    {
        for (int str1 = 1; str1 <= str1Len; ++str1)
        {
            if (str1Input[str1 - 1] == str2Input[str2 - 1])
                vecIsSame[str2][str1] = true;
            else
                vecIsSame[str2][str1] = false;
        }
    }

   for (int str2 = 1; str2 <= str2Len; ++str2)
   {
       for (int str1 = 1; str1 <= str1Len; ++str1)
       {
           if (str1Input[str1 - 1] == str2Input[str2 - 1])
           {
               if (vecIsSame[str2 - 1][str1 - 1])
                   dpCommon[str2][str1] = dpCommon[str2 - 1][str1 - 1] + 1;
               else
                   dpCommon[str2][str1] = 1;
           }
           else
               dpCommon[str2][str1] = 0;
       }
   }

   int maxN = -1;

   for (int str2 = 0; str2 <= str2Len; ++str2)
   {
       for (int str1 = 0; str1 <= str1Len; ++str1)
       {
           if (dpCommon[str2][str1] > maxN)
               maxN = dpCommon[str2][str1];
       }
   }

   cout << maxN << endl;
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