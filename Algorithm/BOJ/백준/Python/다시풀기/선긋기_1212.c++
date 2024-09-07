#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include<queue>
#include<map>
#include <set>
 
#define endl "\n"
#define STR_MAX 10+1
#define CHAR_MAX 26+1
#define INF int(1e9)

using namespace std;

// 시작 시간 기준 정렬
// 매 번, 마지막 끝나는 시점 기록
// 매번 길이 계산
// 현재 끝나는 시간 - 이전 마지막 시점 차이 기록해가기 

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int ans = 0, stTime = 0, edTime = 0;
    int N;
    vector<pair<int, int>> sets;
    sets.reserve(1000000);

    freopen("input_C.txt", "r", stdin);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int St, Ed;
        cin >> St >> Ed;
        sets.push_back(make_pair(St,Ed));
    }
    
    sort(sets.begin(), sets.end());

    for (int i = 0; i < N; i++)
    {
        pair<int, int> c_set = sets[i];
        int c_st = c_set.first, c_ed = c_set.second;
        if (edTime == 0 || edTime < c_st)
            edTime = c_st;
        // cout << "c_st : " << c_st << ", c_ed : " << c_ed << endl;
        if (c_ed <= edTime)
            continue;
        ans += (c_ed - edTime);
        // cout << "c_ed : " <<  c_ed << ", edTime : " << edTime << endl;
        // cout << "ans : " << ans << endl;
        edTime = c_ed;
    }
       
    cout << ans;
    return 0;
}


